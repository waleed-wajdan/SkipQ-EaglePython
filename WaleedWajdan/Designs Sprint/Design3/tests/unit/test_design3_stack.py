import aws_cdk as core
import aws_cdk.assertions as assertions

from design3.design3_stack import Design3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in design3/design3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Design3Stack(app, "design3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
