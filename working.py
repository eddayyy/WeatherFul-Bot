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
            # Write to a local JSON file
            with open("weather_data.json", "w") as json_file:
                json.dump(weather_data, json_file)
                
            temp = weather_data['data'][0]['temp']
            description = weather_data['data'][0]['weather']['description']
            wind_speed = weather_data['data'][0]['wind_spd']
            humidity = weather_data['data'][0]['rh']
            uv_index = weather_data['data'][0]['uv']
            
            return f"Hey Fullerton, it's currently {temp}°F with {description} skies! \n🌬️The current Wind Speeds are: {wind_speed} mph \n💧 We are at {humidity}%\n🌞 UV Index: {uv_index}\nStay comfy and safe! 😊"
        else:
            return "😢 Oops! Couldn't fetch the weather data. Stay tuned for updates! 🌧️"


if __name__ == "__main__":
    weatherful = WeatherfulBot()
    weather_status = weatherful.fetch_weather()
    if weather_status:
        weatherful.create_tweet(weather_status)
