import boto3
import os

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')
    record = event['Records'][0]['Sns']
    print(event)
    
    db_name = os.environ['Wajdan_Alarmtable']
    table = dynamodb.Table(db_name)
    
    response = table.put_item(
        Item={
            'id' : record["MessageId"],
            'Timestamps' : record['Timestamp'],
            'Message' :  record["Message"], 
            'Subject' : record["Subject"]
            
        }
    )