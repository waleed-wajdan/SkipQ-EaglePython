# Welcome to AWS Design Day 5 Python project!


[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)
[![AWS cdk 2.51.1](https://img.shields.io/badge/aws_cdk_lib-2.51.1-yellow.svg)](https://pypi.org/project/aws-cdk-lib/2.51.1/)
[![Constructs 10.1.165](https://img.shields.io/badge/constructs-10.1.165-red.svg)](https://pypi.org/project/constructs/10.1.165/)



## Table of Contents

- [Task](#task)
- [Design](#design)
- [Demo](#demo)


## Task

<b> Design & Develop </b> - Suppose there are 10 files uploading to S3 bucket each day. For each file received on cloud storage, you have a mechanism to process the file. During the processing, your code parses the text and counts the number of times each word is repeated in the file. For example, in the following text: “Hello World and Hello There”, your code should be able to say that "hello" has been used twice, "world" has occurred once and so on. Then it will store the results in some storage and email to some email address after successful processing.


## Design


![image](https://user-images.githubusercontent.com/121339168/235374027-c1bb41f4-5c77-43bf-b8dc-9ab2947eb4f5.png)


## Demo

- <b> Lambda Cloud Watch </b>


File content is "Hello World Hello Audience Hello Reader Bingo Bingo Bingo"



![image](https://user-images.githubusercontent.com/121339168/235374359-ac228a09-a57c-4fba-9d8f-76a924f24294.png)





- <b> S3 bucket for file uploading </b>



![image](https://user-images.githubusercontent.com/121339168/235374375-4b368b36-59b9-4fd9-9bab-c00bb3ae0896.png)





- <b> S3 bucket for output file after we process the data </b>



![image](https://user-images.githubusercontent.com/121339168/235374381-7c889858-4fab-4a37-9df9-8a16bfec6089.png)




- <b> Email notification after output file is uploaded to bucket </b>


![image](https://user-images.githubusercontent.com/121339168/235374292-8ab3ba3a-e397-4747-a158-42f3b209cc82.png)



