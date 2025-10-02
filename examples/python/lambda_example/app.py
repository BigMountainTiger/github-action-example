import json

# This is the simplest lambda example
def lambdaHandler(event, context):
    return {
        'statusCode': 200,
        'body': 'OK'
    }