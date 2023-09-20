import tweepy
import requests
import json
import os
from time import sleep
from dotenv import load_dotenv

class WeatherfulBot: 
        def __init__(self): 
            load_dotenv()
            self.weather_api = os.getenv("WEATHERBIT_API_KEY")
            self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
            
            c_key = os.getenv("TWITTER_CONSUMER_KEY")
            c_secret = os.getenv("TWITTER_CONSUMER_SECRET")
            a_token = os.getenv("TWITTER_ACCESS_TOKEN")
            a_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
            
            # client_id = os.getenv("TWITTER_CLIENT_ID")
            # client_secret = os.getenv("TWITTER_CLIENT_SECRET")
            
            self.client = tweepy.Client(self.bearer_token, c_key, c_secret, a_token, a_secret)
            self.auth = tweepy.OAuth1UserHandler(c_key, c_secret, a_token, a_secret)
            self.api = tweepy.API(self.auth)
            
            
        def create_tweet(self, text):
            self.client.create_tweet(text=text)

        def retweet(self, tweet_id):
            self.client.retweet(tweet_id)
            

        def fetch_weather(self):
            lat = "33.8704"
            lon = "-117.9243"
            url = f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={self.weather_api}&units=I"
            
            response = requests.get(url)
            
            if response.status_code == 200:
                weather_data = json.loads(response.text)
                temp = weather_data['data'][0]['temp']
                description = weather_data['data'][0]['weather']['description']
                return f"The current temperature in Fullerton, CA is {temp}°F. Weather is {description}."
            else:
                return "Could not fetch weather data."

if __name__ == "__main__":
    weatherful = WeatherfulBot()    
    weather_status = weatherful.fetch_weather()
    weather_status = "Test"
    if weather_status:
        weatherful.create_tweet(weather_status)
        