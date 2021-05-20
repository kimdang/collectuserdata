import boto3
from boto3.dynamodb.conditions import Key, Attr
import os

ACCESS_KEY= os.environ['AWS_ACCESS_KEY_ID'] if os.environ['AWS_ACCESS_KEY_ID'] else None
SECRET_KEY= os.environ['AWS_SECRET_ACCESS_KEY'] if os.environ['AWS_SECRET_ACCESS_KEY'] else None
REGION= os.environ['AWS_DEFAULT_REGION'] if os.environ['AWS_DEFAULT_REGION'] else 'us-west-2'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

def add_entry (user_dict):

    table_name = 'tally'

    table = dynamodb.Table(table_name)
    response = table.get_item(
        Key={
            'ID': 1 ## this table only has 1 row
        }
    )

    tallytable = response['Item']

    ## increment
    tallytable[user_dict['browser']] += 1
    tallytable[user_dict['os']] += 1
    tallytable['Totalusers'] += 1

    col_browser = user_dict['browser']
    col_os = user_dict['os']
    col_totusers = 'Totalusers'

    table.update_item(
        Key={
            'ID': 1
        },
        UpdateExpression= "SET %s = :b, %s = :o, %s = :t" %(col_browser, col_os, col_totusers),
        ExpressionAttributeValues = {
            ':b': tallytable[user_dict['browser']],
            ':o': tallytable[user_dict['os']],
            ':t': tallytable['Totalusers']
        },
        ReturnValues = 'UPDATED_NEW'
    )


    return tallytable
