import os
import boto3
import logging

target_dir = "./logs/"

logger = logging.getLogger(__name__) ## get an instance of a logger

def sync_to_s3(target_dir, aws_region=os.environ['AWS_DEFAULT_REGION'], bucket_name=os.environ['BUCKET_NAME']):
    if not os.path.isdir(target_dir):
        raise ValueError('target_dir %r not found.' % target_dir)

    s3 = boto3.resource('s3', region_name=aws_region)
    try:
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration={'LocationConstraint': aws_region})
    except:
        pass

    for filename in os.listdir(target_dir):
        logger.warn('Uploading %s to Amazon S3 bucket %s' % (filename, bucket_name))
        s3.Object(bucket_name, filename).put(Body=open(os.path.join(target_dir, filename), 'rb'))

        logger.info('File uploaded to https://s3.%s.amazonaws.com/%s/%s' % (
            aws_region, bucket_name, filename))


sync_to_s3(target_dir)