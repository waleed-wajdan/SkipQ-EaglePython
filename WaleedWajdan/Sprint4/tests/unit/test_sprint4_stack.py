import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest

from Sprint4.sprint4.sprint4_stack import Sprint4Stack

@pytest.fixture
def stack_template():
    app = core.App()
    stack = Sprint4Stack(app, "sprint4")
    return assertions.Template.from_stack(stack)

def test_s3_bucket_policy_count(stack_template):
    stack_template.resource_count_is("AWS::S3::BucketPolicy", 1)

def test_s3_bucket_count(stack_template):
    stack_template.resource_count_is("AWS::S3::Bucket")

def test_iam_role_count(stack_template):
    stack_template.resource_count_is("AWS::IAM::Role")

def test_iam_policy_count(stack_template):
    stack_template.resource_count_is("AWS::IAM::Policy")

def test_codepipeline_count(stack_template):
    stack_template.resource_count_is("AWS::CodePipeline::Pipeline")
