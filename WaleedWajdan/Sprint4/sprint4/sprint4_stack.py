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
)
from constructs import Construct
from resources import constants as constants

crontim = 60

class Sprint4Stack(Stack):
    # Crontim in seconds

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_role = self.create_lambda_role()
        fn = self.create_lambda("WHLambda",'./resources','WHApp.lambda_handler',lambda_role)
        dbLambda = self.create_lambda("DBLambda",'./resources','DBApp.lambda_handler',lambda_role)
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


    def create_lambda(self,id,asset,handler,role):
        return lambda_.Function(self, id = id, handler = handler, code = lambda_.Code.from_asset(asset), runtime = lambda_.Runtime.PYTHON_3_9,role = role)
    
    def create_lambda_role(self):
        lambdaRole = iam_.Role(self,"Lambda_Role",
            assumed_by = iam_.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [
                iam_.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess")
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