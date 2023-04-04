import boto3
import os
import json
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

client = boto3.resource('dynamodb', region_name='us-east-2')
APITable = os.environ['URL']
table = client.Table(APITable)

def lambda_handler(event, context):

    # taking the http and body from event
    method = event['httpMethod']
    body = event['body']

    # Get Method
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.scan
    if method == 'GET':
        response = table.scan()['Items']
        if response:
            return json_response(response)
        else:
            return json_response({"message": "No such record found"})
    
    # Delete Method
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.delete_item
    elif method == 'DELETE':
        link_id = json.loads(body)['linkId']
        response = table.delete_item(Key={"linkId": str(link_id)})
        if response:
            return json_response({"message": "Url deleted"})
        else:
            return json_response({"message": "URL not found in the table"})
    
    # Post Method
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.put_item
    elif method == 'POST':
        link_id = json.loads(body)["linkId"]
        url = json.loads(body)['URL']
        key = {
            "linkId": str(link_id),
            "URL": url
        }
        try:
            response = table.put_item(
                Item= key,
                ConditionExpression='attribute_not_exists(linkId)'
            )
            if response:
                return json_response({"message": "URL added successfully"})
        except ClientError as error:
            if error.response['Error']['Code'] == 'ConditionalCheckFailedException':
                return json_response({"message": "LinkID already exists"})
    

    # Put Method
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.update_item
    elif method == 'PUT':
        link_id = json.loads(body)['linkId']
        url = json.loads(body)['URL']
        response = table.update_item(
                    Key={"linkId": str(link_id)},
                    UpdateExpression = 'SET #u=:url',
                    ConditionExpression='attribute_not_exists(deletedAt)',
                    ExpressionAttributeValues = {":url": url},
                    ExpressionAttributeNames={"#u": "URL"},
                    ReturnValues="UPDATED_NEW"
                )
        if response:
            return json_response({"message": "URL updated successfully"})
        else:
            return json_response({"message": "URL not found"})
    
    # returning invalid method message to client
    else:
        return json_response({"message": "Invalid. Valid methods are: GET, DELETE, POST, PUT"})


# Response Method
def json_response(res):
    return {
        "statusCode": 200,
        "body": json.dumps(res),
        "headers": {'Content-Type': 'application/json'}
    }


