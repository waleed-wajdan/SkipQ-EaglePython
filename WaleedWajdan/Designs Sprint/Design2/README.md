# Welcome to AWS Design Day 2 Python project!


[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)
[![AWS cdk 2.51.1](https://img.shields.io/badge/aws_cdk_lib-2.51.1-yellow.svg)](https://pypi.org/project/aws-cdk-lib/2.51.1/)
[![Constructs 10.1.165](https://img.shields.io/badge/constructs-10.1.165-red.svg)](https://pypi.org/project/constructs/10.1.165/)



## Table of Contents

- [Task](#task)
- [Design](#design)
- [Installation](#installation)
- [Demo](#demo)


## Task

Consider that you are getting events in the format [{"event1":{"attr1": value }}] from different APIs.
* How will you parse the event to get the value?
* How will you return 10 latest events when required?


## Design


## Demo

- <b> API POST Request </b>

![image](https://user-images.githubusercontent.com/121339168/235370565-c22de830-9111-4614-87a8-348b09041032.png)


- <b> API GET Request </b>

![image](https://user-images.githubusercontent.com/121339168/235370572-a4a9006e-5139-43bd-a795-a1606117b2e0.png)


- <b> Dynamo DB table </b>

![image](https://user-images.githubusercontent.com/121339168/235370609-d0d1a644-a779-42b1-86dd-acedb3acfdb5.png)


