import boto3

region = 'ap-southeast-1' ##AWS Region
instances = ['i-08ef35f0d42ebd8c4'] ## EC2 instance ID

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances) ## Call Start Instance
    print('start your instances: ' + str(instances))
