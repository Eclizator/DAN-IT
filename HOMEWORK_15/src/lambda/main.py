import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Define the tag key and value
    tag_key = 'eclizator'
    tag_value = 'stop'
    
    # Find instances with the specific tag
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': f'tag:{tag_key}',
                'Values': [tag_value]
            }
        ]
    )
    
    # Collect instance IDs
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    # Stop the instances
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped instances: {instance_ids}')
    else:
        print('No instances to stop')
    
    return {
        'statusCode': 200,
        'body': f'Stopped instances: {instance_ids}'
    }