from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_iam as iam_,
    aws_events as events_,
    aws_events_targets as target_,
    RemovalPolicy,
    aws_cloudwatch as cw_,
    aws_sns as sns_,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as cw_actions,
    aws_dynamodb as db_,
    aws_codedeploy as codedeploy_,
    aws_apigateway as apigateway_,
)
from constructs import Construct
from resources import constants as constants

crontim = 60

class Sprint5Stack(Stack):
    # Crontim in seconds

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_role = self.create_lambda_role('sprint5_stackpy')
        fn = self.create_lambda("WHLambda",'./resources','WHApp.lambda_handler',lambda_role)
        dbLambda = self.create_lambda("DBLambda",'./resources','DBApp.lambda_handler',lambda_role)
        APILambda = self.create_lambda("APILambda",'./resources','APIApp.lambda_handler',lambda_role)
       

        duration_metric = fn.metric_duration()
        invocation_metric = fn.metric_invocations()

        duration_alarm = cw_.Alarm(self, "Duration_Metric_Errors",
                comparison_operator=cw_.ComparisonOperator.GREATER_THAN_THRESHOLD,
                threshold=200000,
                evaluation_periods= 60,
                metric= duration_metric
                )
        
        invocation_alarm = cw_.Alarm(self, "Invocation_Metric_Errors",
                comparison_operator=cw_.ComparisonOperator.GREATER_THAN_THRESHOLD,
                threshold=5,
                evaluation_periods= 60,
                metric= invocation_metric
                )


        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_codedeploy/LambdaDeploymentConfig.html
        version = fn.current_version
        alias = lambda_.Alias(self, "VersionAlias",
            alias_name="prod",
            version=version
            )

        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_codedeploy/LambdaDeploymentConfig.html
        deployment_group = codedeploy_.LambdaDeploymentGroup(self, "FirstDeploymentGroup",
                            # application=application,
                            alarms = [duration_alarm,invocation_alarm],
                            alias=alias,
                            auto_rollback = codedeploy_.AutoRollbackConfig(deployment_in_alarm=True),
                            deployment_config=codedeploy_.LambdaDeploymentConfig.LINEAR_10_PERCENT_EVERY_1_MINUTE
                        )

        target = target_.LambdaFunction(handler=fn)
        rule = events_.Rule(self, "WHAppRule",
        schedule = events_.Schedule.rate(Duration.minutes(crontim)),
        targets = [target]
        )
        fn.apply_removal_policy(RemovalPolicy.DESTROY)
        rule.apply_removal_policy(RemovalPolicy.DESTROY)


        topic = sns_.Topic(self,"WHNotifications")
        topic.add_subscription(subscriptions_.EmailSubscription('waleed.khan.skipq@gmail.com'))
        topic.add_subscription(subscriptions_.LambdaSubscription(dbLambda))
        

        for i in range(4):
            dimensions = {'URL': constants.url[i]}

            availability_metric = cw_.Metric(
                metric_name = constants.AvailabilityMetric,
                namespace = constants.namespace,
                dimensions_map = dimensions
            )

            availability_alarm = (cw_.Alarm(
                self, 
                "Availability_of_" + constants.url[i],
                metric = availability_metric,
                evaluation_periods=crontim,
                threshold=1,
                comparison_operator=cw_.ComparisonOperator.LESS_THAN_THRESHOLD
            ))
            availability_alarm.add_alarm_action(cw_actions.SnsAction(topic))

            latency_metric = (cw_.Metric(
                metric_name = constants.LatencyMetric,
                namespace = constants.namespace,
                dimensions_map = dimensions
            ))

            latency_alarm = (cw_.Alarm(
                self, 
                "Latency_of_" + constants.url[i],
                metric = latency_metric,
                evaluation_periods=crontim,
                threshold=0.5,
                comparison_operator=cw_.ComparisonOperator.GREATER_THAN_THRESHOLD
            ))
            latency_alarm.add_alarm_action(cw_actions.SnsAction(topic))

        dbTable = self.create_dynamodb_table()
        dbTable.grant_read_write_data(dbLambda)
        dbLambda.add_environment('Wajdan_Alarmtable',dbTable.table_name)

        APITable = self.create_API_table()
        APITable.grant_read_write_data(APILambda)
        APILambda.add_environment('URL',APITable.table_name)
        fn.add_environment('URL', APITable.table_name)
        APILambda.grant_invoke(iam_.ServicePrincipal("apigateway.amazonaws.com"))

        api = apigateway_.LambdaRestApi(self, "WaleedWajdanAPI",
                                        handler=APILambda,
                                        proxy=False,
                                        endpoint_configuration=apigateway_.EndpointConfiguration(
                                                                types=[apigateway_.EndpointType.REGIONAL]
                                                            )
                                        )

        # CRUD methods
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/LambdaRestApi.html
        items = api.root.add_resource("items")
        items.add_method("GET")
        items.add_method("POST")
        items.add_method("DELETE")
        items.add_method("PUT")

    def create_lambda(self,id,asset,handler,role):
        return lambda_.Function(self, id = id, handler = handler, code = lambda_.Code.from_asset(asset), runtime = lambda_.Runtime.PYTHON_3_9,role = role,timeout=Duration.minutes(5))
    
    def create_lambda_role(self,uniqname):
        lambdaRole = iam_.Role(self,"Lambda_Role"+uniqname,
            assumed_by = iam_.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [
                iam_.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonAPIGatewayInvokeFullAccess")
            ])
        return lambdaRole
    
    def create_dynamodb_table(self):
        table = db_.Table(
            self,
            "Wajdan_Alarmtable",
            partition_key = db_.Attribute(name = "id", type = db_.AttributeType.STRING),
            removal_policy = RemovalPolicy.DESTROY,
            sort_key = db_.Attribute(name = "Timestamps", type = db_.AttributeType.STRING)
        )
        return table
    
    def create_API_table(self):
        table = db_.Table(self, "WaleedWajdan-API_Url_Table",
            partition_key = db_.Attribute(name="linkId", type=db_.AttributeType.STRING),
            removal_policy = RemovalPolicy.DESTROY
        )
        return table