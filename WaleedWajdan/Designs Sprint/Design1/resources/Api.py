from cloudwatch_putData import AWSCloudWatch

def lambda_handler(event, context):
    
    cloudwatch_object = AWSCloudWatch()
    
    body = event["body"]
    value = int(body)
    
    """ Sending data to CloudWatch"""
    dimensions = [{'Name': 'arg1','Value': str(value)}]

    cloudwatch_object.cloudwatch_metric_data("WajdanDesign1Space" , "WajdanDesign1Metric" , dimensions, value)

    if event["httpMethod"] == "PUT":
        response = {
            "statusCode": 200,
            "body": event["body"],
        }

        return response