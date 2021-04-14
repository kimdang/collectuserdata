import boto3
import credential
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', aws_access_key_id=credential.AWS_ACCESS_KEY_ID, aws_secret_access_key=credential.AWS_SECRET_ACCESS_KEY, region_name=credential.AWS_DEFAULT_REGION)

table = dynamodb.Table('collectuserinfo')

resp = table.get_item(
    Key={
        'browser': 'Ngan'
    }
)

if 'Item' in resp:
    print(resp['Item'])