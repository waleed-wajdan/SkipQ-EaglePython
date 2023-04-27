import aws_cdk as cdk
from aws_cdk import (
    Stack,
    pipelines as pipelines_,
    aws_codepipeline_actions as actions_,
)
from constructs import Construct

from sprint5.WaleedWajdanStage import WaleedWajdanSprint5Stage

class WaleedWajdanPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = pipelines_.CodePipelineSource.git_hub('waleed12022skipq/EaglePython','main', 
                                                       authentication= cdk.SecretValue.secrets_manager("AmazonGithub1"),
                                                       trigger = actions_.GitHubTrigger('POLL')
                                                    )
        synth = pipelines_.ShellStep('WaleedWajdanPipelineStackShellStepSynthID', 
                                     input = source,                        
                                    commands = ['cd WaleedWajdan/Sprint5/',
                                    'npm install -g aws-cdk',
                                    'pip install -r requirements.txt',
                                    'cdk synth'],
                                    primary_output_directory = 'WaleedWajdan/Sprint5/cdk.out')
        
        pipeline = pipelines_.CodePipeline(self, 'WaleedWajdanSprint5PipelineStackShellStepPipelineID', synth = synth)

        betaTesting = WaleedWajdanSprint5Stage(self, "WajdanBetaStage")
        prod = WaleedWajdanSprint5Stage(self, "WajdanProdStage")

        pipeline.add_stage(betaTesting, pre = [

                                    pipelines_.ShellStep('WaleedWajdanPipelineStackShellStepSynthID', 
                                    input = source,                        
                                    commands = ['cd WaleedWajdan/Sprint5/',
                                    'npm install -g aws-cdk',
                                    'pip install boto3',
                                    'pip install -r requirements.txt',
                                    'pip install -r requirements-dev.txt',
                                    'cdk synth',
                                    "pytest"],
                                    primary_output_directory = 'WaleedWajdan/Sprint5/cdk.out')
        ])
        pipeline.add_stage(prod, pre = [pipelines_.ManualApprovalStep("PromotetoProd")])
