# Welcome to AWS Design Day 3!


## Table of Contents

- [Task 1](#task-1)
- [Task 2](#task-2)


## Task 1
#### Question 1:
<b> How would you automate deployment (e-g on AWS) for a system that has source code in a repo.? </b>

The deployment can be automated by using a repo-change based approach. We can utilize a CI/CD pipeline. The pipeline has following stages:
- <b> Source stage: </b> When code is pushed into the repo, the CI/CD pipeline is triggered. Every time we change the repo with a changed/new code, the execution process starts again.
- <b> Build/Test Stage: </b> Code is built and synthesized in this stage. We can set up stages for testing.
- <b> Deploy Stage: </b> If the tests are passed successfully, then the code is deployed.


#### Question 2:
<b> How do we generate an artifact from the repo that gets published and later is used in some services.? </b>
- An artifact is generated using CodeBuild within the pipeline. 
- The artifacts are stored in a S3 bucket.
- Artifacts can be shared using a unique URL that allows external and internal usage of the artifact.


#### Question 3: 
<b> Are there more than one solutions? </b>

We can utilize multiple methods to achieve almost anything generating the same result when working with AWS. For example, we could directly download the artifacts from the AWS console.

## Task 2
Deploy, maintain and rollback pipeline for an artifact deployment e-g lambda package, docker image etc.

![Rollback](https://user-images.githubusercontent.com/121339168/234926442-11dd865d-af16-4768-8821-9f252cefd05e.png)

#### Question 1:
<b> If the latest deployment is failing, why do you think that is.? </b>

Some possible reasons are:
- Not assigning necessary AWS roles.
- Pipeline does not have access to the repository.
- Maybe some items have expired that were available for the last run.
- There is a internal conflict that can only be resolved by deleting the stack and redeploying..

#### Question 2:
<b> How will you rollback.? </b>

We can rollback using version control and having stages in the pipeline. We can make tests that our code needs to pass to get to the deployment stage. We can also keep a record of say the last 3 versions that we can deploy instead to get back to a previous state.


#### Question 3:
<b> How do you reduce such failures so there is less need to rollback.? </b>

We can reduce such failures by having multiple stages with different tasks/tests and making the code modular. Additionally we can make the deployment limited to specific users for testing instead of having to rollback for the entire userbase if an issue comes up.
