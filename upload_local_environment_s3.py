import os
import boto3
import requests

os.environ.setdefault('AWS_DEFAULT', 'dataengineer-itvgithub')

s3_client = boto3.client('s3')
s3_objects = s3_client.list_objects(
    Bucket='dataengineer-itvgithub'
)
file = '2022-09-27-15.json.gz'
res = requests.get(f'https://data.gharchive.org/{file}')

upload_res = s3_client.put_object(
    Bucket='dataengineer-itvgithub',
    Key='2015-01-01-15.json.gz',
    Body=res.content
)

print(upload_res)
