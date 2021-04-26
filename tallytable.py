import boto3
import credential
from boto3.dynamodb.conditions import Key, Attr



dynamodb = boto3.resource('dynamodb', aws_access_key_id=credential.AWS_ACCESS_KEY_ID, aws_secret_access_key=credential.AWS_SECRET_ACCESS_KEY, region_name=credential.AWS_DEFAULT_REGION)



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
     