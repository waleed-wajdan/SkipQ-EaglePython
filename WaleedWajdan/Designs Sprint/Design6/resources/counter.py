import boto3
import re
from collections import Counter
import os
import json

def lambda_handler(event, context):
    
    # Parsing the bucket for name and key
    bucketname = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object
    client = boto3.client('s3')
    response = client.get_object(Bucket= bucketname, Key=filename)
    given = response['Body'].read().decode()

    # Counting the number of occurences of each word
    temp = re.sub(r'\W+', ' ', given)
    res = temp.split()
    count_data = Counter(res)

    print(count_data)

    # Calling output S3 bucket from environment variables and setting file name for our output file
    output_bucket = os.environ['S3Bucket']
    output_filename = "output_" + filename

    # Converting our data to bytes 
    uploadByteStream = bytes(json.dumps(count_data).encode('UTF-8'))

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object
    client.put_object(Bucket=output_bucket, Key=output_filename, Body=uploadByteStream)

    print("Succesfully uploaded")
    return count_data