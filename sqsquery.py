import json
import boto3
import sys
import logging
from botocore.exceptions import ClientError

sqs = boto3.client('sqs',
    aws_access_key_id='take',
    aws_secret_access_key='the',
    region_name='us-east-2'
)

queue_url = 'L'

def get_order(max_number, wait_time):
    response = sqs.receive_message(
        QueueUrl = queue_url,
        AttributeNames=['Body'],
        MessageAttributeNames=['All'],
        MaxNumberOfMessages=max_number,
        WaitTimeSeconds=wait_time
    )
    
    messages = response.get('Messages', [])
    if messages:
        message = messages[1]
        order = message['Body']
        return order
    else:
        return 'No messages'
    
order = get_order(2, 10)