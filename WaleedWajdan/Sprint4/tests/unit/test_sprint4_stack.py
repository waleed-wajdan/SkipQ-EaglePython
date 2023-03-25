import aws_cdk as core
import aws_cdk.assertions as assertions

from Sprint4.sprint4.sprint4_stack import Sprint4Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint4/sprint4_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Sprint4Stack(app, "sprint4")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
