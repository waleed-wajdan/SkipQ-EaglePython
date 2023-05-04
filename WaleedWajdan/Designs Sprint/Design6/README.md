# Welcome to AWS Design Day 6 !


## Table of Contents

- [Task](#task)
- [Design](#design)


## Task

<b> Design </b> Client needs a Notification System – that notifies the Admins about report summaries, users about operations within the system, and notifies clients/users about any changes. What AWS service(s) would you use for such a system?



## Design

![image](https://user-images.githubusercontent.com/121339168/235376429-57e5dc14-68a1-41b8-9584-c6cb4a377c93.png)

## Demo

- <b> Lambda Cloud Watch Logs for Admin </b>

![image](https://user-images.githubusercontent.com/121339168/235377150-f0df106c-7829-48e7-abdd-33595c8a9571.png)


- <b> Email Notification after successful upload in output bucket for Users </b>

![image](https://user-images.githubusercontent.com/121339168/235376945-a8a271fb-5ba9-4e2b-878e-c1782fdc60ee.png)


- <b> API POST Trigger by associating Lambda with the API </b>

![image](https://user-images.githubusercontent.com/121339168/235376933-e124a444-9d7c-401b-a143-fb1930f2ba4d.png)


- <b> Email notification to inform Admin about activity in the API Gateway and associated logs </b>

![image](https://user-images.githubusercontent.com/121339168/235376918-9c91aec7-3465-42cd-a793-a55d36be666f.png)
