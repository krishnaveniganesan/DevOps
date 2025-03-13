import boto3

def lambda_handler(event, context):
    region = event.get('region', 'us-east-1')
    ec2 = boto3.client('ec2', region_name=region)

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Environment', 'Values': ['dev']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    instances = [
        instance['InstanceId']
        for reservation in response['Reservations']
        for instance in reservation['Instances']
    ]

    if not instances:
        return {'statusCode': 400, 'body': 'No stopped instances with tag env=dev found'}

    ec2.start_instances(InstanceIds=instances)
    return {'statusCode': 200, 'body': f'Started instances: {instances}'}
