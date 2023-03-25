import aws_cdk as cdk
from aws_cdk import (
    Stage,
)
from constructs import Construct

from sprint4.sprint4_stack import Sprint4Stack

class WaleedWajdanSprint4Stage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.stage = Sprint4Stack(self, 'WaleedWajdanStage')