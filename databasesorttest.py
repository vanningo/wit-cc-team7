import boto3
import json
import logging
from collections import defaultdict
import botocore
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MysfitsTable')

response = table.query( 
    TableName="MysfitsTable",
    IndexName="Status-Likes-index",
   KeyConditionExpression=Key('Status').eq("OK"),
    ScanIndexForward=False)
    

items = response['Items']
for item in items:
    print(item)

print("\n\n///\n\n")

response = table.query( 
    TableName="MysfitsTable",
    IndexName="Status-Likes-index",
   KeyConditionExpression=Key('Status').eq("OK"),
    ScanIndexForward=True)
    

items = response['Items']
for item in items:
    print(item)