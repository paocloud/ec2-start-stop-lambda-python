import boto3

region = 'ap-southeast-1'
instances = ['i-08ef35f0d42ebd8c4']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
