import boto3
import credential
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', aws_access_key_id=credential.AWS_ACCESS_KEY_ID, aws_secret_access_key=credential.AWS_SECRET_ACCESS_KEY, region_name=credential.AWS_DEFAULT_REGION)

user_dict = {
    'browser': 'Chrome', 
    'os' : 'Windows'
}

table_name = 'tally'

table = dynamodb.Table(table_name)
response = table.get_item(
    Key={
        'ID': 1 ## this table only has 1 row
    }
)

ini_tally = response['Item']
print(ini_tally)

ini_tally[user_dict['browser']] += 1
ini_tally[user_dict['os']] += 1

table.update_item(
    Key={
        'ID': 1
    }
    UpdateExpression= 'SET '
)