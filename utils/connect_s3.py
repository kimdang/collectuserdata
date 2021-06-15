import os, sys
import boto3
import botocore
from SQSQueue import Queue
import datetime


BASE_DIR = BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_dir = BASE_DIR + "/logs/"

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID', None)
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
REGION = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')
BUCKETNAME = os.getenv('BUCKET_NAME', None)
QueueName = os.getenv('QUEUE_NAME', None)

def sync_to_s3(target_dir=target_dir, aws_region=REGION, bucket_name=BUCKETNAME, ACCESS_KEY=ACCESS_KEY, QueueName=QueueName, SECRET_KEY=SECRET_KEY):
    now = datetime.datetime.now()
    print(f"Begin syncing to s3 bucket {now}.")

    ## check if directory exists
    if not os.path.isdir(target_dir):
        raise ValueError('Directory target_dir %r not found.' % target_dir)

    s3 = boto3.resource('s3', region_name=aws_region)

    ## create bucket if not exists
    try:
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration={'LocationConstraint': aws_region})
    except:
        pass
    
    queue = Queue(REGION=aws_region, ACCESS_KEY=ACCESS_KEY, SECRET_KEY=SECRET_KEY, QueueName=QueueName)


    ## upload all log files to s3 bucket
    for filename in os.listdir(target_dir):
        try:
            s3.Object(bucket_name=bucket_name, key=filename).load()
            sys.stdout.write(f'{filename} already exists in s3 bucket. \n')
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                s3.Object(bucket_name=bucket_name, key=filename).put(Body=open(os.path.join(target_dir, filename), 'rb'))
                ## send filename and bucketname to queue
                queue.send_message(filename, bucket_name)
                sys.stdout.write(f'{filename} is uploaded to s3 bucket. \n')
            else:
                sys.stdout.write(f'{filename} cannot be uploaded to s3 bucket. \n')


if __name__ == "__main__":
    sync_to_s3()
