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
        
        c_key = os.getenv("TWITTER_CONSUMER_KEY")
        c_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        
        a_token = os.getenv("TWITTER_ACCESS_TOKEN")
        a_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        
        client_id = os.getenv("TWITTER_CLIENT_ID")
        client_secret = os.getenv("TWITTER_CLIENT_SECRET")
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        
        self.client = tweepy.Client(self.bearer_token, c_key, c_secret, a_token, a_secret)
        auth = tweepy.OAuth1UserHandler(c_key, c_secret, a_token, a_secret)
        self.api = tweepy.API(auth)
        
        
    def create_tweet(self, text):
        self.client.create_tweet(text=text)

    def retweet(self, tweet_id):
        self.client.retweet(tweet_id)
        

if __name__ == "__main__":
    weatherful = WeatherfulBot()
    weatherful.create_tweet("Testing 1, 2, 3")




