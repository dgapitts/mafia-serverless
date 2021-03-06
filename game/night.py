import os, sys
# to read dependencies from ./lib direcroty
script_dir = os.path.dirname( os.path.realpath(__file__) )
sys.path.insert(0, script_dir + os.sep + "lib")
import logging, boto3, json, random

# for dynamodb filter queries
from boto3.dynamodb.conditions import Key, Attr

# setup log level to DEBUG
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMO_TABLE'])

# Night murder is happening here
def handler(event, context): 
  return response( {"Message": "Welcome to the Serverless Workshop fully powered by AWS Lambda elastic cloud computing service"}, event)


def mafia_win_message():
  return {
    "Message": [
      "Game Over!", 
      "All innocent people has been killed by Mafia",
      "Mafia have won this game!"
    ]}


def response(body, event, code=200):
  if 'resource' in event and 'httpMethod' in event:
    return {
        'statusCode': code,
        'headers': {},
        'body': json.dumps(body, indent=4, separators=(',', ':')) 
      }
  return body

