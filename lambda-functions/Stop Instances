import boto3

def lambda_handler(event, context):
    region = event.get('region', 'us-east-1')
    ec2 = boto3.client('ec2', region_name=region)

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Environment', 'Values': ['dev']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    instances = [
        instance['InstanceId']
        for reservation in response['Reservations']
        for instance in reservation['Instances']
    ]

    if not instances:
        return {'statusCode': 400, 'body': 'No running instances with tag env=dev found'}

    ec2.stop_instances(InstanceIds=instances)
    return {'statusCode': 200, 'body': f'Stopped instances: {instances}'}
