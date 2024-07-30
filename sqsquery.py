import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os

load_dotenv()

sqs = boto3.client('sqs',
    aws_access_key_id = os.getenv('SQS_ACCESS_KEY'),
    aws_secret_access_key = os.getenv('SQS_SECRET_ACCESS_KEY'),
    region_name='us-east-2'
)

queue_url = os.getenv('SQS_URL')

def get_order(wait_time):
    response = sqs.receive_message(
        QueueUrl = queue_url,
        AttributeNames=['Body'],
        MessageAttributeNames=['All'],
        WaitTimeSeconds=wait_time
    )
    
    messages = response.get('Messages', [])
    #need to add proper error handling for failed requests
    for x in range(5):
        if messages:
            message = messages[x]
            order = message['Body']
            return order
        else:
            return 'No messages'
        
#print(get_order(10))