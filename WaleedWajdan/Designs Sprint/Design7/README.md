# Welcome to AWS Design Day 7 Python project!


[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)
[![AWS cdk 2.51.1](https://img.shields.io/badge/aws_cdk_lib-2.51.1-yellow.svg)](https://pypi.org/project/aws-cdk-lib/2.51.1/)
[![Constructs 10.1.165](https://img.shields.io/badge/constructs-10.1.165-red.svg)](https://pypi.org/project/constructs/10.1.165/)



## Table of Contents

- [Task](#task)
- [Design](#design)
- [Demo](#demo)


## Task

<b> Design & Develop </b> - What if we have a 15MB file that we have to upload on S3 using API gateway. We have the limitation that our API gateway has the maximum payload capacity of 10MB. How will you solve this problem?


## Design


![image](https://user-images.githubusercontent.com/121339168/235378275-0a7150d3-41af-417c-aa0a-9ea652cc11e6.png)


## Demo

- <b> Rest API to get pre-signed url for uploading the file </b>


![image](https://user-images.githubusercontent.com/121339168/235378528-5dc76886-efdf-4edc-a10c-d956e9ad623a.png)



- <b> Item in S3 Bucket </b>


![image](https://user-images.githubusercontent.com/121339168/235378499-8c7439cc-f1e2-4033-a913-d8265d9868c0.png)


