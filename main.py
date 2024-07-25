import json
import click
import boto3
import sys
import logging
from botocore.exceptions import ClientError

#cli takes in 2 orders at a time
#if chef 1 is busy, then try chef 2
#if chef 1 and chef 2 are busy then add a to a queue (FIFO), display count of the queue

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
    
    
def print_banner():
    return """
\033[91m  ____  _                \033[0m\033[92m ____  _                 \033[0m
\033[91m |  _ \(_)__________ _   \033[0m\033[92m/ ___|| |__   ___  _ __  \033[0m
\033[91m | |_) | |_  /_  / _` |  \033[0m\033[92m\___ \| '_ \ / _ \| '_ \ \033[0m
\033[97m |  __/| |/ / / / (_| |  \033[0m\033[97m ___) | | | | (_) | |_) |\033[0m
\033[97m |_|   |_/___/___\__,_|  \033[0m\033[97m|____/|_| |_|\___/| .__/ \033[0m
\033[97m                         \033[0m\033[97m                  |_|    \033[0m
    """

order = get_order(2, 10)

@click.command()
def cli():
    click.echo(print_banner())
    if order:
        click.echo(order)

if __name__ == '__main__':
    cli()