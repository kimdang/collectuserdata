import boto3
from boto3.dynamodb.conditions import Key, Attr
import os 



dynamodb = boto3.resource('dynamodb', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name=os.environ['AWS_DEFAULT_REGION'])



def add_entry (user_dict):

    table_name = 'tally'

    table = dynamodb.Table(table_name)
    response = table.get_item(
        Key={
            'ID': 1 ## this table only has 1 row
        }
    )

    tallytable = response['Item']


    ## check if columns exist and add as necessary
    for col in [user_dict['browser'], user_dict['os'], 'Totalusers']:
        if col not in tallytable.keys():
            tallytable[col] =  1
        else:
            tallytable[col] += 1


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
     
