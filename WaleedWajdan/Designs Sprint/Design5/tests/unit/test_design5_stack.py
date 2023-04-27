import aws_cdk as core
import aws_cdk.assertions as assertions

from design5.design5_stack import Design5Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in design5/design5_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Design5Stack(app, "design5")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
