from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_iam as iam_,
    aws_s3 as s3_,
    aws_s3_notifications as s3n_,
    aws_sns as sns_,
    aws_sns_subscriptions as subscription_,
    RemovalPolicy,
)
from constructs import Construct

class Design5Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = self.create_lambda_role()
        fn = self.create_lambda("InputProcessing", "./resources", "counter.lambda_handler",lambda_role)
        fn.apply_removal_policy(RemovalPolicy.DESTROY)

        # Creating s3 buckets and giving read write permission for our lambda function 
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_s3/README.html
        bucket = s3_.Bucket(self, "WajdanDesign5Bucket1")
        bucket.grant_read_write(fn)

        output_bucket = s3_.Bucket(self, "WajdanDesign5Bucket2")
        output_bucket.grant_read_write(fn)

        # Adding output bucket to environment variable
        fn.add_environment('S3Bucket',output_bucket.bucket_name)

        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_sns_subscriptions/EmailSubscription.html

        topic = sns_.Topic(self, "NotificationDesign5")
        topic.add_subscription(subscription_.EmailSubscription("waleed.khan.skipq@gmail.com"))

        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_s3_notifications/README.html
        bucket.add_event_notification(s3_.EventType.OBJECT_CREATED, s3n_.LambdaDestination(fn))

        # Email notification on upload 
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_s3_notifications/README.html
        output_bucket.add_event_notification(s3_.EventType.OBJECT_CREATED_PUT, s3n_.SnsDestination(topic))


    def create_lambda(self,id , asset , handler , role):
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
            managed_policies = [iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
                                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                                iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess")]
            )
        return lambdaRole
