import boto3

#Get session:
aws_mag_con=boto3.session.Session(profile_name="terraform")
#Specify resource to use:
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)
