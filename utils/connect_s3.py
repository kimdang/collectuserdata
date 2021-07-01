import os, sys, datetime
import boto3, botocore
from SQSQueue import Queue


BASE_DIR = BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_dir = BASE_DIR + "/logs/"


aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', None)
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', None)
region_name = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')
BucketName = os.getenv('BUCKET_NAME', None)
QueueName = os.getenv('QUEUE_NAME', None)



def sync_to_s3(target_dir=target_dir, resgion_name=region_name, BucketName=BucketName, aws_access_key_id=aws_access_key_id, QueueName=QueueName, aws_secret_access_key=aws_secret_access_key):
    now = datetime.datetime.now()
    print(f"Begin syncing to s3 bucket {now}.")

    ## check if directory exists
    if not os.path.isdir(target_dir):
        raise ValueError('Directory target_dir %r not found.' % target_dir)

    s3 = boto3.resource('s3', region_name=region_name)

    ## create bucket if not exists
    try:
        s3.create_bucket(Bucket=BucketName,
                         CreateBucketConfiguration={'LocationConstraint': region_name})
    except:
        pass
    
    queue = Queue(region_name, aws_access_key_id, aws_secret_access_key, QueueName)


    ## upload all log files to s3 bucket
    for filename in os.listdir(target_dir):
        try:
            s3.Object(bucket_name=BucketName, key=filename).load()
            sys.stdout.write(f'{filename} already exists in s3 bucket. \n')
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                s3.Object(bucket_name=BucketName, key=filename).put(Body=open(os.path.join(target_dir, filename), 'rb'))
                ## send filename and bucketname to queue
                queue.send_message(filename, BucketName)
                sys.stdout.write(f'{filename} is uploaded to s3 bucket. \n')
            else:
                sys.stdout.write(f'{filename} cannot be uploaded to s3 bucket. \n')



def get_from_s3(info, region_name=region_name):
    s3 = boto3.resource('s3', region_name=info.region_name)
    try:
        s3.Object(bucket_name=info.BucketName, key=info.filename).load()
        
    except KeyError:
        sys.stdout.write(f'{info.filename} does not exist in bucket {info.Bucketname}.')




if __name__ == "__main__":
    sync_to_s3()
