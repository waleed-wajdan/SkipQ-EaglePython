import aws_cdk as core
import aws_cdk.assertions as assertions

from design2.design2_stack import Design2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in design2/design2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Design2Stack(app, "design2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
