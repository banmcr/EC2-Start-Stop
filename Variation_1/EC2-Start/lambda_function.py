import boto3

def lambda_handler(event, context):
    region = 'ap-south-1'
    ec2 = boto3.client('ec2', region_name=region)
    for i in ['i-0acba12a3c632d4d4']:
        response = ec2.describe_instance_status(InstanceIds=[i])
        print(i)
        if response['InstanceStatuses'] != []:
            print('running')
#    print(response)
        else:
            ec2.start_instances(InstanceIds=[i])
            print('server started')
        
#   print('started your instances: ' + str(instances)) 