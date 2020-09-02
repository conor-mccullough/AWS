import boto3
#credentials:
aws_mag_con = boto3.session.Session(profile_name="terraform")
#iam, ec2, s3

#client connections:
iam_con_cli = aws_mag_con.client(service_name="iam", region_name="us-east-1")
ec2_con_cli = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
s3_con_cli = aws_mag_con.client(service_name="s3", region_name="us-east-1")

"""
#List all IAM users using client object

response = iam_con_cli.list_users()
print(response)
print("Provides all the default information in the response syntax in bulk")
print("\n")
print("\n")

for each_item in response['Users']:
# Prints each item individually:
#    print(each_item)

# Prints just the UserName element from within the User
    print(each_item['UserName'])


### Look at the official boto3 docs to see the heirarchy of each item in commands
"""

#Display all EC2 instance ID's

response2 = ec2_con_cli.describe_instances()
#print(response2['Reservations'])

for each_item in response2['Reservations']:
    for each_instance in each_item['Instances']:
        print(each_instance['InstanceId'])
    print('-------------------------------')
