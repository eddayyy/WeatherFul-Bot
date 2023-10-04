import json
from main import MainProgram


def lambda_handler(event=None, context=None):
    main = MainProgram()
    main.run('hourly')
    print("Successful Run!\n")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
