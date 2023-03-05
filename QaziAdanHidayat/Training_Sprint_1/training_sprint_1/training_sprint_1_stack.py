from aws_cdk import (
    aws_lambda as lambda_,
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class TrainingSprint1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        fn = self.createLambda("HelloLambda",'./resources','HelloLambda.lambda_handler')
    

    def createLambda(self,id,asset,handler):
        return lambda_.Function(self, 
        id = id,
        handler = handler,
        code=lambda_.Code.from_asset(asset),
        runtime=lambda_.Runtime.PYTHON_3_9
        
        )
        