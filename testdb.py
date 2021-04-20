import boto3
import credential
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', aws_access_key_id=credential.AWS_ACCESS_KEY_ID, aws_secret_access_key=credential.AWS_SECRET_ACCESS_KEY, region_name=credential.AWS_DEFAULT_REGION)
## table = boto3.client('dynamodb') ## you can use client API or resource API, resource API is higher level.

table_name = 'tally'

def create_table(table_name):
    existed_tables = [table.name for table in dynamodb.tables.all()]

    if table_name not in existed_tables:
        table = dynamodb.create_table(TableName=table_name, KeySchema=[
            {
                'AttributeName': 'IP_address', 
                'KeyType': 'HASH' ## partition key
            }, 
            {
                'AttributeName': 'timestamp', 
                'KeyType': 'RANGE' ## sort key
            }
        ], 
        AttributeDefinitions=[
            {
                'AttributeName': 'IP_address', 
                'AttributeType': 'S', 
            }, 
            {
                'AttributeName': 'timestamp', 
                'AttributeType': 'S'
            }
        ], 
        ProvisionedThroughput={
            'ReadCapacityUnits': 5, 
            'WriteCapacityUnits': 5
        })
        table.wait_until_exists()
        print(table_name + ' has been created.')
    else:
        print(table_name + ' already existed in database.')


def delete_table(table_name):
    table = dynamodb.Table(table_name)
    table.delete()
    table.wait_until_not_exists()
    print(table_name + " has been deleted.")

def add_item(table_name):
    table = dynamodb.Table(table_name)
    table.put_item(
        Item={
            'IP_address': '12.345.67.123',
            'timestamp': '2012-04-18 03:45:00', 
            'other': {
                'os': 'chrome', 
                'browser': 'safari'
            }
    })




