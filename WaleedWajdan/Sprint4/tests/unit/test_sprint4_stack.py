import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest
import boto3

from resources import constants
from sprint4.sprint4_stack import Sprint4Stack

@pytest.fixture
def stack_template():
    app = core.App()
    stack = Sprint4Stack(app, "sprint4")
    return assertions.Template.from_stack(stack)

def test_s3_bucket_policy_count(stack_template):
    stack_template.resource_count_is("AWS::IAM::Role", 1)

def test_s3_bucket_count(stack_template):
    stack_template.resource_count_is("AWS::Lambda::Function",2)

def test_iam_role_count(stack_template):
    stack_template.resource_count_is("AWS::Lambda::Permission",2)

def test_iam_policy_count(stack_template):
    stack_template.resource_count_is("AWS::SNS::Subscription",2)

def test_codepipeline_count(stack_template):
    stack_template.resource_count_is("AWS::Events::Rule",1)





@pytest.fixture(scope="function")
def cfn_stack():
    """Create a CloudFormation stack for the `Sprint4Stack`."""
    stack_name = "Sprint4StackFunctionalTest"
    app = core.App()
    Sprint4Stack(app, stack_name)
    return boto3.resource("cloudformation").Stack(stack_name)

def test_cloudwatch_alarms(cfn_stack):
    """Verify that CloudWatch alarms are created for each URL."""
    cloudwatch = boto3.client("cloudwatch")
    alarms = cloudwatch.describe_alarms()
    for url in constants.url:
        availability_alarm_name = "Availability_of_{}".format(url)
        latency_alarm_name = "Latency_of_{}".format(url)
        assert any(a["AlarmName"] == availability_alarm_name     for a in alarms["MetricAlarms"])
        assert any(a["AlarmName"] == latency_alarm_name for a in alarms["MetricAlarms"])

def test_dynamodb_table(cfn_stack):
    """Verify that data can be written and read from the DynamoDB table."""
    dynamodb = boto3.resource("dynamodb")
    table_name = cfn_stack.outputs["Sprint4Stack.DBTableName"]
    table = dynamodb.Table(table_name)

    # Write data to the table
    item = {
        "id": "test",
        "Timestamps": "2022-01-01T00:00:00.000000",
        "data": "some test data",
    }
    table.put_item(Item=item)

    # Read the data from the table
    response =  table.get_item(Key={'id': 'test'})
    assert(response == table.get_item(Key={'id': 'test'}))


