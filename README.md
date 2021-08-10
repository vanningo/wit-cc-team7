## "Sort-a" Mysfits
http://wit-cc-a5-ngov.s3-website-us-east-1.amazonaws.com/

## Introduction
Mythical Mysfits is a pet adoption website dedicated to fictional creatures. We've added functionality to the website to increase sorting options as well as to gain an understanding on user actions through recording what they click. We've also attempted to increase the security of our application using AWS Cognito + AWS Certificate Manager, though these could not be implemented due to AWS Educate restrictions. 


## Features
1. User Registration
2. Logging In/Logging Out
3. View/Filter Mysfits
4. Like/Adopt Mysfits
5. Record User Clicks


## System Architecture
![alt text](https://raw.githubusercontent.com/vanningo/wit-cc-team7/main/Picture1.png)


## Deployment
1. Login to AWS Educate (or normal AWS account)
2. Use Cloud9 IDE and clone this repository to your IDE
3. View website files under /aws-modern-application-workshop/module-5
4. View test of sorting feature under /test/databasesorttest.py
5. Create a bucket using the command below, replacing 'REPLACE_ME_BUCKET_NAME' with your bucket:

```
aws s3 mb s3://REPLACE_ME_BUCKET_NAME
```
6. Deploy all files in /aws-modern-application-workshop/module-3/web with this command:

```
aws s3 cp --recursive ~/environment/aws-modern-application-workshop/module-5/web/ s3://REPLACE_ME_BUCKET_NAME
```
7. Update S3 bucket policy and visit your website to see the changes
8. Create sort-key in DynamoDB and add a new field to the table called "Status" and set it to "OK" for every Mysfit


# Demo video 



Sample: https://www.youtube.com/watch?v=Pr-JMqTkdEM

How to record your screen: https://www.techradar.com/how-to/record-your-screen
## References
https://www.programcreek.com/python/example/103723/boto3.dynamodb.conditions.Key

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html

https://stackoverflow.com/questions/45632961/aws-dynamodb-boto3-query-group-by-and-order-by

https://stackoverflow.com/questions/64674100/boto3-dynamodb-query-all-data-with-limit-and-order-by

https://stackoverflow.com/questions/56136226/how-to-get-most-recent-data-from-dynamodb-for-each-primary-partition-key

https://github.com/aws-samples/aws-modern-application-workshop


## Team members 
Vanni Ngo (ngov@wit.edu), Team Lead, Frontend/Backend Dev

Mark Noble (noblej2@wit.edu), Team Member, Researcher
