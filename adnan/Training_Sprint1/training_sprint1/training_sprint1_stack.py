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
        fn = lambda_.Function(self, "Hello_Lambda",
                runtime=lambda_.Runtime.PYTHON_3_9,
                handler="hellowordLambda.lambda_Handler",
                code=lambda_.Code.from_asset('./resources'))

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "TrainingSprint1Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
