from aws_cdk import (
    aws_lambda as lambda_,
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
import boto3


class Sprint1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = self.create_lambda("HelloWorldLambda", "HelloWorldLambda.lambda_handler", lambda_.Runtime.PYTHON_3_8, "resources")

    def create_lambda(self, name, handler, runtime, asset_path="resources"):
        return lambda_.Function(self, name,
                                runtime=runtime,
                                handler=handler,
                                code=lambda_.Code.from_asset(asset_path),
                                )

