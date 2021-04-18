import boto3
import credential
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', aws_access_key_id=credential.AWS_ACCESS_KEY_ID, aws_secret_access_key=credential.AWS_SECRET_ACCESS_KEY, region_name=credential.AWS_DEFAULT_REGION)
## table = boto3.client('dynamodb') ## you can use client API or resource API, resource API is higher level 


def create_table():
    table_name = "test_collectuserinfo"
    existed_tables = [table.name for table in dynamodb.tables.all()]

    if table_name not in existed_tables:
        table = dynamodb.create_table(TableName=table_name, KeySchema=[
            {
                'AttributeName': 'IP_address', 
                'KeyType': 'HASH' ## partition key
            }, 
            {
                'AttributeName': 'access_time', 
                'KeyType': 'RANGE' ## sort key
            }
        ], 
        AttributeDefinitions=[
            {
                'AttributeName': 'IP_address', 
                'AttributeType': 'N'
            }, 
            {
                'AttributeName': 'access_time', 
                'AttributeType': 'S'
            }

        ], 
        ProvisionedThroughput={
            'ReadCapacityUnits': 5, 
            'WriteCapacityUnits': 5
        })

        table.meta.client.get_waiter('table_exists').wait(TableName='users')
    else:
        print(table_name + ' already existed in database!')




def 

create_table()