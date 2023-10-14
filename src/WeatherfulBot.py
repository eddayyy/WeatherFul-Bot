import os
import logging

from dotenv import load_dotenv
from TwitterClient import TwitterClient
from WeatherClient import WeatherClient


class WeatherfulBot:
    def __init__(self):
        load_dotenv()
        logging.basicConfig(level=logging.INFO)

        try:
            bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
            c_key = os.getenv("TWITTER_API_KEY")
            c_secret = os.getenv("TWITTER_API_KEY_SECRET")
            a_token = os.getenv("TWITTER_ACCESS_TOKEN")
            a_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
            weather_api = os.getenv("WEATHERBIT_API_KEY")

            if not all([bearer_token, c_key, c_secret, a_token, a_secret, weather_api]):
                raise ValueError("Missing essential environment variable")

            self.twitter_client = TwitterClient(
                bearer_token, c_key, c_secret, a_token, a_secret
            )

            self.weather_client = WeatherClient(
                city='Fullerton,California',
                weather_api=weather_api
            )
        except ValueError as e:
            logging.error(f"Configuration Error: {e}")
            raise

    def validate_tweet(self, tweet_text):

        return len(tweet_text) <= 280

    def tweet(self, type):
        if type == 'hourly':
            tweet_text = self.weather_client.fetch_weather()
        elif type == 'sun':
            tweet_text = self.weather_client.fetch_sun_times()
        elif type == 'weekly':
            tweet_text = self.weather_client.fetch_weekly_forecast()

        if self.validate_tweet(tweet_text):
            self.twitter_client.create_tweet(tweet_text)
