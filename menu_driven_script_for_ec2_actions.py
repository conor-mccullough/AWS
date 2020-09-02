import boto3
import sys
from pprint import pprint
import time
aws_mag_con=boto3.session.Session(profile_name='terraform')
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name='us-east-1')
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name='us-east-1')
response=ec2_con_cli.describe_instances()['Reservations']

for each_item in response:
    print("Printing instances...")
    for each in each_item['Instances']:
        print("==================================")
        print('Instance ID: {}\nInstance monitoring: {}\nInstance state: {}'.format(each['InstanceId'],each['Monitoring'],each['State']))

while True:

    print("This script performs the following actions on an EC2 instance:")
    print("""
    1. Start
    2. Stop
    3. Terminate
    4. Exit""")

    opt=int(input("Enter your option: "))
    if opt == 1:
        instance_id=input("Enter your instance ID: ")
        my_req_instance=ec2_con_re.Instance(instance_id)
# Displays functions available for use with the defined instance:
#        print(dir(my_req_instance))
        print("Starting EC2 instance")
        my_req_instance.start()
    elif opt == 2:
        instance_id=input("Enter your instance ID: ")
        my_req_instance=ec2_con_re.Instance(instance_id)
        my_req_instance.stop()
        print("Stopping EC2 instance")
    elif opt == 3:
        instance_id=input("Enter your instance ID: ")
        my_req_instance=ec2_con_re.Instance(instance_id)
        my_req_instance.terminate()
        print("Terminating EC2 instance")
    elif opt == 4:
        time.sleep(10)
        sys.exit()
    else:
        print("Your option is invalid. Please select a valid option.")
time.sleep(5)
