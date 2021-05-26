import boto3
from boto3.dynamodb.conditions import Key, Attr
import os 

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID', None)
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
REGION = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')

dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)



def add_entry (user_dict):

    try:
        table_name = 'tally'

        table = dynamodb.Table(table_name)
        response = table.get_item(
            Key={
                'ID': 1 ## this table only has 1 row
            }
        )
        tallytable = response['Item']

    except:
        tallytable = {}



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
     
