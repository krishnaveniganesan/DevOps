import boto3

def lambda_handler(event, context):
    ec2_instance_details = find_running_instances()
    rds_instance_details = find_available_rds_instances()

    email_body = (
        "Dear Team,\n\n"
        "Below is a list of the current instances and RDS available in various regions. "
        "If any of these instances are not actively in use, please proceed to turn them off. "
        "This action will contribute to cost savings and help maintain an efficient AWS environment.\n\n"
        f"Running EC2 Instances:\n{ec2_instance_details}\n\n"
        f"Available RDS Instances:\n{rds_instance_details}\n\n"
        "Sincerely, \n"
        "Cloud Team"
    )

    send_email(email_body)

def find_running_instances():
    try:
        ec2_client = boto3.client('ec2')
        regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
        instances = []

        for region in regions:
            try:
                client = boto3.client('ec2', region_name=region)
                response = client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
                instances += [
                    f"Region: {region}, Instance ID: {instance['InstanceId']}"
                    for reservation in response['Reservations']
                    for instance in reservation['Instances']
                ]
            except Exception as e:
                print(f"Error in region {region}: {e}")

        return "\n".join(instances)

    except Exception as e:
        print(f"Error fetching running instances: {e}")
        return 'Error fetching running instances.'

def find_available_rds_instances():
    try:
        regions = [region['RegionName'] for region in boto3.client('ec2').describe_regions()['Regions']]
        rds_instances = {}

        for region in regions:
            try:
                rds_client = boto3.client('rds', region_name=region)
                instances = [
                    f"Region: {region}, Instance ID: {instance['DBInstanceIdentifier']}, Status: {instance['DBInstanceStatus']}"
                    for instance in rds_client.describe_db_instances()['DBInstances']
                    if instance['DBInstanceStatus'] == 'available'
                ]
                rds_instances[region] = instances
            except Exception as e:
                print(f"Error in region {region}: {e}")

        return "\n".join([instance for instances in rds_instances.values() for instance in instances])

    except Exception as e:
        print(f"Error fetching available RDS instances: {e}")
        return 'Error fetching available RDS instances.'

def send_email(email_body):
    try:
        ses_client = boto3.client('ses')
        sender_email = 'your-email@example.com'  # Replace with your email
        recipient_emails = ['recipient1@example.com', 'recipient2@example.com']  # Update recipient list
        subject = 'AWS Resources Alert'

        response = ses_client.send_email(
            Source=sender_email,
            Destination={'ToAddresses': recipient_emails},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': email_body}},
            }
        )

        print(f"Email sent! Message ID: {response['MessageId']}")

    except Exception as e:
        print(f"Error sending email: {e}")
