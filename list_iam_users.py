import boto3

#Get session:
aws_mag_con=boto3.session.Session(profile_name="terraform")
#Specify resource to use:
s3_con=aws_mag_con.resource('s3')

for bucket in s3_con.buckets.all():
    print(bucket)
