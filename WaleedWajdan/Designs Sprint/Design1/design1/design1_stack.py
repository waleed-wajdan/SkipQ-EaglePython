from aws_cdk import (
    Duration,
    aws_lambda as  lambda_,
    aws_iam as iam_,
    Stack,
    aws_sns as sns_,
    aws_sns_subscriptions as subscription_,
    aws_apigateway as apigateway_,
    # aws_sqs as sqs,
)

from constructs import Construct

class Design1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = self.create_lambda_role()
        api_lambda = self.create_lambda("ApiLambda", "./resources", "Api.lambda_handler",lambda_role)

        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/LambdaRestApi.html

        api = apigateway_.LambdaRestApi(self, "Wajdan_Design1",
                                        handler=api_lambda,
                                        proxy=False,
                                        )
        
        Email_response = api.root.add_resource("EmailResponse")
        Email_response.add_method("PUT")

        """SNS Subscription"""
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_sns_subscriptions/EmailSubscription.html

        topic = sns_.Topic(self, "Design1")
        topic.add_subscription(subscription_.EmailSubscription("waleed.khan.skipq@gmail.com"))

        topicarn = topic.topic_arn
        api_lambda.add_environment('sns_arn',topicarn)

    #Creating the Lambda Function
    def create_lambda(self, id , asset , handler , role):
            return lambda_.Function(self,
            id = id,
            code=lambda_.Code.from_asset(asset),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler=handler,
            role = role,
            timeout=Duration.minutes(5))
    
    #Creating a Lambda Role Object for giving permissions
    def create_lambda_role(self):
        lambdaRole = iam_.Role(self, "lambda-role",
            assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [
                                iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonAPIGatewayInvokeFullAccess")
                                ]
            )
        return lambdaRole
