from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as  lambda_,
    aws_iam as iam_,
    aws_apigateway as apigateway_,
    aws_dynamodb as db_,
    RemovalPolicy,
    # aws_sqs as sqs,
)
from constructs import Construct

class Design2Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = self.create_lambda_role()
        api_lambda = self.create_lambda("ApiLambda", "./resources", "Api.lambda_handler",lambda_role)

        api_design_table = self.create_api_table()
        api_design_table.grant_read_write_data(api_lambda)
        api_lambda.add_environment('TableName',api_design_table.table_name)


        # Defining API gateway Rest Apis
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/LambdaRestApi.html

        api_1 = apigateway_.LambdaRestApi(self, "WajdanDesign2",
                                        handler=api_lambda,
                                        proxy=False,
                                        )
        
        # Adding resource and method in Api 
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/LambdaRestApi.html
        items = api_1.root.add_resource("root")
        items.add_method("GET")
        items.add_method("POST")

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
                                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess")
                                ]
            )
        return lambdaRole
    

    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_dynamodb/README.html
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_dynamodb/Attribute.html#aws_cdk.aws_dynamodb.Attribute

    def create_api_table(self):
        table = db_.Table(self, "Design2",
            partition_key = db_.Attribute(name="attr1", type=db_.AttributeType.STRING),
            removal_policy = RemovalPolicy.DESTROY,
            sort_key = db_.Attribute(name="requestTime",type=db_.AttributeType.STRING),
        )
        return table