import boto3
from pprint import pprint

aws_mag_con=boto3.session.Session(profile_name="terraform")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

#response=ec2_con_cli.describe_instances()['Reservations']
"""
for each_item in response:
    for each in each_item['Instances']:
        pprint("The Image Id is: {}\nThe Instance Id is: {}\nThe Instance Launch Time is: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime']))
"""

response = ec2_con_cli.describe_volumes()['Volumes']

pprint(response)
#Every useable option will be in the output here.

print("\n")
print("==========================================================")
print("\n")

""" The following doesn't work for some reason - the tutorial didn't get into it:
for each_item in response:
    for each in each_item['Attachments']:
        pprint("The Volume Id is: {}\nThe next value is {}".format(each_item['AttachTime'],each_item['VolumeId']))
"""
for each_item in response:
    print('The Volume Id is: {} \nThe AZ is {}\nThe State is: {}'.format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['State']))
