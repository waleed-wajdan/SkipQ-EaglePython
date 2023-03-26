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

# Functional Test
def test_create_lambda():
    app = core.App()
    stack = Sprint4Stack(app, "sprint4")

    # create lambda function
    lambda_role = stack.create_lambda_role()
    lambda_function = stack.create_lambda("TestLambda", "./resources", "test_lambda.handler", lambda_role)

    # assert function properties
    assert lambda_function.function_name == "TestLambda"
    assert lambda_function.handler == "test_lambda.handler"
    assert lambda_function.role == lambda_role
    assert lambda_function.runtime == lambda_.Runtime.PYTHON_3_9

# Integration Test
def test_sprint4_stack():
    app = core.App()
    stack = Sprint4Stack(app, "test-stack")

    # deploy the stack
    core.Tags.of(stack).add("env", "test")
    core.Tags.of(stack).add("project", "sprint4")
    app.synth()

    # assert resources were created
    assert stack
    assert stack.lambda_role
    assert stack.availability_alarm_of_url0
    assert stack.availability_alarm_of_url1
    assert stack.availability_alarm_of_url2
    assert stack.availability_alarm_of_url3
    assert stack.latency_alarm_of_url0
    assert stack.latency_alarm_of_url1
    assert stack.latency_alarm_of_url2
    assert stack.latency_alarm_of_url3
    assert stack.topic
    assert stack.db_table




