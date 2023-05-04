import aws_cdk as core
import aws_cdk.assertions as assertions

from design6.design6_stack import Design6Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in design6/design6_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Design6Stack(app, "design6")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
