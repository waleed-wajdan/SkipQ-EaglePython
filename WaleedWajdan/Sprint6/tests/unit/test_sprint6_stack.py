import aws_cdk as core
import aws_cdk.assertions as assertions

from sprint6.sprint6_stack import Sprint6Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint6/sprint6_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Sprint6Stack(app, "sprint6")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
