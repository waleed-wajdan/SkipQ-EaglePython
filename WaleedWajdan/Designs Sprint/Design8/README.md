# Welcome to AWS Design Day 8 !


## Table of Contents

- [Task](#task)
- [Design](#design)


## Task

You are a DevOps engineer working at a big tech company and your manager has given you a task to migrate a three-tier PHP-based monolithic application to microservices. Consider the scenario that the application is running on a EC2 server with ALB in front of it. Now design an E2E architecture that would containerize the application.

Expectation:

How the application would be migrated to microservices

Need a running application of container based services

The application should have an E2E CI/CD pipeline that would build the application and deploy the updated code/manifest on the container-based services

Design the above architecture in draw.io 
 




## Design

### Basic outlook of a microservices based app

![image](https://user-images.githubusercontent.com/121339168/235538140-d5481f6e-00b7-4ce9-9f9a-faa99b420482.png)


### Operation of the Monolithic Application

![image](https://user-images.githubusercontent.com/121339168/236127031-8bf35a33-38bb-4bd6-92bd-33ab6d2ba256.png)


### Containerization of the Monolith into its different services i.e. microservices architecture

![image](https://user-images.githubusercontent.com/121339168/236127314-ff4fdfeb-7de8-4e15-9bc5-6a2e1f908a45.png)


### Our monolithic application migrated to microservices

![image](https://user-images.githubusercontent.com/121339168/236127465-51161727-fbc4-4975-a499-f3bcf12c7d06.png)
