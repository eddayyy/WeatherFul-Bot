import json
from WeatherfulBot import WeatherfulBot


def lambda_handler(event, context):
    weather = WeatherfulBot()
    method = event.get('method', 'hourly')

    if method == 'hourly':
        weather.tweet('hourly')
    elif method == 'weekly':
        weather.tweet('weekly')
    elif method == 'sun':
        weather.tweet('sun')

    return {
        'statusCode': 200,
        'body': json.dumps(f'Method {method} executed successfully')
    }
