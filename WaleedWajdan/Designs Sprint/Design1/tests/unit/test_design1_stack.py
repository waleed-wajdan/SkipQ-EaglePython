import aws_cdk as core
import aws_cdk.assertions as assertions

from design1.design1_stack import Design1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in design1/design1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Design1Stack(app, "design1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
