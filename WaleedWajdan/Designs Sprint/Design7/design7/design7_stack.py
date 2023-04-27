from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
    Stack,
    aws_iam as iam_,
    aws_apigateway as apigateway_,
    aws_s3 as s3_,
)
from constructs import Construct

class Design7Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = self.create_lambda_role()
        fn = self.create_lambda("BigFileLambda", "./resources", "Bigfile.lambda_handler",lambda_role)

        # Creating Rest API
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/LambdaRestApi.html

        api = apigateway_.LambdaRestApi(self, "WajdanDesign7api",
                                        handler=fn,
                                        proxy=False,
                                        )

        # Adding resources
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/LambdaRestApi.html
        items = api.root.add_resource("Bigfile")
        items.add_method("GET")

        # Creating S3 bucket 
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_s3/README.html
        bucket = s3_.Bucket(self, "WajdanDesign7")
        bucket.grant_read_write(fn)

        # Adding bucket to environment variable
        fn.add_environment('Design7Bucket',bucket.bucket_name)

    def create_lambda(self, id , asset , handler , role):
        return lambda_.Function(self,
        id = id,
        code=lambda_.Code.from_asset(asset),
        runtime=lambda_.Runtime.PYTHON_3_9,
        handler=handler,
        role = role,
        timeout=Duration.minutes(5))
    
    def create_lambda_role(self):
        lambdaRole = iam_.Role(self, "lambda-role",
            assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [
                                iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonAPIGatewayInvokeFullAccess"),
                                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),                                
                                ]
            )
        return lambdaRole