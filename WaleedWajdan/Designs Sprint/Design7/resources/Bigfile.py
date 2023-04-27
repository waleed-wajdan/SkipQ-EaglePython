import boto3
import os
import json

client = boto3.client('s3', region_name ='us-east-2')
bucket = os.environ['Design7Bucket']

def lambda_handler(event, context):

    # Passing the bucket to our presigned_post function
    # and getting presigned url for s3 bucket
    object_name = 'design7.png'
    bucket_name = bucket
    method = event['httpMethod']
    response = create_presigned_post(bucket_name, object_name, 36000)

    if method == "GET":
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {'Content-Type': 'application/json'}
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Invalid method"}),
            'headers': {'Content-Type': 'application/json'}
        }


# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file
def create_presigned_post(bucket_name, object_name, expiration):

    # Generate a presigned S3 POST URL
    try:
        response = client.generate_presigned_post(Bucket = bucket_name,
                                                  Key = object_name,
                                                  ExpiresIn = expiration)
    except ClientError as e:
        logging.error(e)
        return None

    return response