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

        fn = self.create_lambda("HelloLambda","./resources","HelloWorldLambda.lambda_handler")

    def create_lambda(self, id, asset, handler):
        return lambda_.Function(self,
        id = id,
        handler = handler,
        code=lambda_.Code.from_asset(asset),
        runtime=lambda_.Runtime.PYTHON_3_9)
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "TrainingSprint1Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
