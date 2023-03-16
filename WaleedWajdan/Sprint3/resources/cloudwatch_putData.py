import boto3

class AWSCloudWatch:
    def __init__(self) -> None:
        self.client = boto3.client('cloudwatch')    

    def cloudwatch_metric_data(self, namespace,metric_name, dimensions, value):
        
        response = self.client.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': dimensions,
                    'Value': value,
                }
            ]
        )