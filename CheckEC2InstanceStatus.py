import boto3

region = 'ap-southeast-1'
instances = ['i-08ef35f0d42ebd8c4']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    response = ec2.describe_instance_status(InstanceIds=instances)
    print(response['InstanceStatuses'][0]['InstanceState']['Name'])
