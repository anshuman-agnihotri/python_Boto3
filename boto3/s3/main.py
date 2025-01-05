import boto3
client = boto3.client('s3')
response = client.create_bucket(
    ACL='private', 
    Bucket='dev87587645',
   
    ObjectOwnership='BucketOwnerPreferred' 
)
print(response)