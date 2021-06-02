import os
import boto3

target_dir = "../logs/"

def sync_to_s3(target_dir=target_dir, aws_region=os.environ['AWS_DEFAULT_REGION'], bucket_name=os.environ['BUCKET_NAME']):
    if not os.path.isdir(target_dir):
        raise ValueError('target_dir %r not found.' % target_dir)

    s3 = boto3.resource('s3', region_name=aws_region)
    try:
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration={'LocationConstraint': aws_region})
    except:
        pass

    for filename in os.listdir(target_dir):
        s3.Object(bucket_name, filename).put(Body=open(os.path.join(target_dir, filename), 'rb'))

sync_to_s3(target_dir)