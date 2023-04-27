import aws_cdk as cdk
from aws_cdk import (
    Stage,
)
from constructs import Construct

from sprint5.sprint5_stack import Sprint5Stack

class WaleedWajdanSprint5Stage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.stage = Sprint5Stack(self, 'WaleedWajdanStage')