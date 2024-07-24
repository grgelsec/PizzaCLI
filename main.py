import json
import click
import boto3

#cli takes in 2 orders at a time
#if chef 1 is busy, then try chef 2
#if chef 1 and chef 2 are busy then add a to a queue (FIFO), display count of the queue

sqs = boto3.client('sqs',
    aws_access_key_id='take',
    aws_secret_access_key='the',
    region_name='us-east-2'
)

queue_url = 'L'

def place_order(order):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(order)
    )

def get_order():
    response = sqs.receive_message(
        QueueUrl = queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10
    )

    messages = response.get('Messages', [])
    if messages: 
        message = message[0]
        receipt_handle = message['ReceiptHandle']
        order = json.loads(message['Body'])
        print(f"Received order: {order}")

         # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        return order
    else:
        print("No orders available")
        return None
    
def print_banner():
    return """
\033[91m  ____  _                \033[0m\033[92m ____  _                 \033[0m
\033[91m |  _ \(_)__________ _   \033[0m\033[92m/ ___|| |__   ___  _ __  \033[0m
\033[91m | |_) | |_  /_  / _` |  \033[0m\033[92m\___ \| '_ \ / _ \| '_ \ \033[0m
\033[97m |  __/| |/ / / / (_| |  \033[0m\033[97m ___) | | | | (_) | |_) |\033[0m
\033[97m |_|   |_/___/___\__,_|  \033[0m\033[97m|____/|_| |_|\___/| .__/ \033[0m
\033[97m                         \033[0m\033[97m                  |_|    \033[0m
    """
place_order({"type:" "Cheese"})

order = get_order()
@click.command()
def cli():
    click.echo(print_banner())
    if order:
        click.echo(order)

if __name__ == '__main__':
    cli()