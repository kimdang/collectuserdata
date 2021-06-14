""" 
use for learning and testing SQS only!!!!
"""


import boto3 
import os 
import json

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID', None)
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
REGION = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')

sqs = boto3.resource('sqs', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

URL = 'https://sqs.us-west-2.amazonaws.com/689543408395/MyTestQueue'

queue = sqs.get_queue_by_name(QueueName='MyTestQueue')
message_bodies = []
messages_to_delete = []

# response = queue.send_message(MessageBody="Hello Bitch!")

for message in queue.receive_messages(MaxNumberOfMessages=10):
    # body = json.loads(message.body)
    message_bodies.append(message.body)
    
    messages_to_delete.append({
        'Id': message.message_id, 
        'ReceiptHandle': message.receipt_handle,
    })

print(message_bodies)


def send_message()
    text = 
    response = queue.send_message(
        MessageBody={

        }
    )


if __name__ = "__main__":
