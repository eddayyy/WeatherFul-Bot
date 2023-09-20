import tweepy
import requests
import json
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
weatherbit_api_key = os.getenv("WEATHERBIT_API_KEY")
twitter_consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
twitter_consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Configure Tweepy
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
api = tweepy.API(auth)

def fetch_weather():
    # Latitude and Longitude for Fullerton, CA
    lat = 33.8704
    lon = -117.9244
    
    # Fetch weather data using latitude and longitude
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}'
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        main_data = data['main']
        weather_data = data['weather'][0]
        
        temperature = main_data['temp'] - 273.15  # Convert from Kelvin to Celsius
        description = weather_data['description']
        
        return f'The current weather in Fullerton, CA is {temperature:.2f}°C with {description}.'
    else:
        return None

while True:
    tweet = fetch_weather()
    
    if tweet:
        api.update_status(tweet)
        print(f'Tweeted: {tweet}')
        
    sleep(3600)  # Sleep for 1 hour (3600 seconds)
