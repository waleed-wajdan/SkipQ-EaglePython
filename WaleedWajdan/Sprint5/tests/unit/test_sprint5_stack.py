import aws_cdk as core
from aws_cdk import aws_iam as iam_
import aws_cdk.assertions as assertions
import pytest
import boto3
import json

from resources import constants
from sprint5.sprint5_stack import Sprint5Stack
from resources import WHApp

@pytest.fixture
def stack():
    app = core.App()
    stack = Sprint5Stack(app, "sprint5test")
    return stack
    app.synth()

@pytest.fixture
def stack_template():
    app = core.App()
    stack = Sprint5Stack(app, "sprint5")
    return assertions.Template.from_stack(stack)

def test_s3_bucket_policy_count(stack_template):
    stack_template.resource_count_is("AWS::IAM::Role", 3)

def test_s3_bucket_count(stack_template):
    stack_template.resource_count_is("AWS::Lambda::Function",3)

def test_iam_role_count(stack_template):
    stack_template.resource_count_is("AWS::Lambda::Permission",11)

def test_iam_policy_count(stack_template):
    stack_template.resource_count_is("AWS::SNS::Subscription",2)

def test_codepipeline_count(stack_template):
    stack_template.resource_count_is("AWS::Events::Rule",1)

def test_RestAPI(stack_template):
    stack_template.resource_count_is("AWS::ApiGateway::RestApi", 1)

# Functional Test
def test_constants():
    result = constants
    assert result.url == ['google.com','github.com','amazon.com','youtube.com']
    assert result.namespace == "WajdanNamespace"
    assert result.AvailabilityMetric == "Availability"
    assert result.LatencyMetric == "Latency"

def test_WHApp(stack):
    lambda_role = stack.create_lambda_role('WHApptest')
    test = stack.create_lambda("WHTestLambda",'./resources','WHApp.lambda_handler',lambda_role)
    assert test
    

# Integration Test
def test_sprint5_stack(stack):
    app = core.App()

    # deploy the stack
    core.Tags.of(stack).add("env", "test")
    core.Tags.of(stack).add("project", "sprint5")
    app.synth()

    # assert resources were created
    assert stack