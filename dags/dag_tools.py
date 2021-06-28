from utils.SQSQueue import Queue
import os

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', None)
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', None)
region_name = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')
BucketName = os.getenv('BUCKET_NAME', None)
QueueName = os.getenv('QUEUE_NAME', None)

def get_queue(region_name, aws_access_key_id, aws_secret_access_key, QueueName):
    queue = Queue(region_name, aws_access_key_id, aws_secret_access_key, QueueName)
    queue.receive_message()
    return



if __name__ == '__main__':
    get_queue(region_name, aws_access_key_id, aws_secret_access_key, QueueName)