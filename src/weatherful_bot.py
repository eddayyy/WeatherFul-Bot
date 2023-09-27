import tweepy
import requests
import json
import os
import pytz

from datetime import datetime, timezone
from time import sleep
from dotenv import load_dotenv


class WeatherfulBot:
    def __init__(self):
        '''
        Initialize the WeatherfulBot class.

        Attributes:
            - lat, lon: Coordinates for location
            - weather_api, bearer_token: API keys
            - client, auth, api: Tweepy API handlers
        '''

        # Load and set API keys
        load_dotenv()
        self.weather_api = os.getenv("WEATHERBIT_TRIAL_API_KEY")
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

        # Load Twitter credentials
        c_key = os.getenv("TWITTER_CONSUMER_KEY")
        c_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        a_token = os.getenv("TWITTER_ACCESS_TOKEN")
        a_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        # Initialize Tweepy API handlers
        self.client = tweepy.Client(
            self.bearer_token, c_key, c_secret, a_token, a_secret)
        self.auth = tweepy.OAuth1UserHandler(
            c_key, c_secret, a_token, a_secret)
        self.api = tweepy.API(self.auth)

        # Initialize location attributes (Fullerton, CA)
        self.lon = "-117.9243"
        self.lat = "33.8704"

        # Failure text
        self.failure_text = "😢 Oops! Couldn't fetch the weather data. Stay tuned for updates! 🌧️"

    def validate_tweet(self, tweet_text):
        '''
        Validate a tweet's text length.

        Parameters:
            - tweet_text: The text to be validated

        Returns:
            - True if the tweet is valid, False otherwise
        '''
        return len(tweet_text) <= 280

    def create_tweet(self, text):
        '''
        Create a new tweet.

        Parameters:
            - text: The text content of the tweet
        '''
        try:
            # Attempt to create a tweet
            self.client.create_tweet(text=text)
        except tweepy.TweepyException as e:
            # e is an instance of TweepError
            print(f"Error code: {e.add_note}, Error message: ")

    def fetch_weather(self):
        '''
        Fetch current weather data for a specific location and format it into a tweet.

        Returns:
            - A string containing the tweet text if successful, or an error message if not.
        '''

        url = f"https://api.weatherbit.io/v2.0/current?lat={self.lat}&lon={self.lon}&key={self.weather_api}&units=I"
        response = requests.get(url)

        # Check if the API call was successful
        if response.status_code == 200:

            weather_data = json.loads(response.text)
            temp = weather_data['data'][0]['temp']
            description = weather_data['data'][0]['weather']['description']
            wind_speed = weather_data['data'][0]['wind_spd']
            humidity = weather_data['data'][0]['rh']
            uv_index = weather_data['data'][0]['uv']

            # Create the tweet text
            fetch_weather_text = f"Hey Fullerton, it's currently {temp}°F with {description}! \n🌬️The current Wind Speeds are: {wind_speed} mph \n💧 We are at {humidity}% humidity\n🌞 UV Index: {uv_index}\nStay comfy and safe! 😊"
            return fetch_weather_text
        else:
            return f"Weather API Error Code: {response.status_code} {response.reason}"

    def fetch_weekly_forecast(self):
        '''
        Fetch the 7-day weather forecast and format it into a tweet.

        Returns:
            - A string containing the tweet text if successful, or an error message if not.
        '''
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?lat={self.lat}&lon={self.lon}&key={self.weather_api}&units=I&days=7"
        response = requests.get(url)

        if response.status_code == 200:
            forecast_data = json.loads(response.text)
            tweet_text = "Here's the 7-day weather outlook for Fullerton 🌞🌧️:"

            for day in forecast_data['data']:
                full_date = day['valid_date']
                date_obj = datetime.strptime(full_date, "%Y-%m-%d")
                day_of_week = date_obj.strftime("%A")
                date = full_date[5:]

                max_temp = int(day['high_temp'])
                min_temp = int(day['low_temp'])
                description = day['weather']['description']

                # Including the day of the week, date, and some emojis
                new_line = f"\n🗓 {day_of_week} ({date}): 🌡 {max_temp}/{min_temp}°F, {description}"

                # Check if the tweet text is too long
                if len(tweet_text + new_line) > 280:
                    break

                tweet_text += new_line
            return tweet_text
        else:
            # Return the error message and status code if the API call fails
            error_message = f"Failed to fetch the weekly forecast. Error code: {response.status_code}"
            print(error_message)
            return error_message

    def fetch_sun_times(self):
        '''
        Fetch and tweet sunrise and sunset times.

        Returns:
            - String: Formatted sunrise and sunset times or error message.
        '''

        # Construct the API URL for fetching sun times
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?lat={self.lat}&lon={self.lon}&key={self.weather_api}&units=I"

        # Fetch sunrise and sunset data
        response = requests.get(url)

        # Process the response if successful (HTTP 200)
        if response.status_code == 200:
            sun_data = json.loads(response.text)

            # Verify that data exists
            if 'data' in sun_data and sun_data['data']:
                first_day_data = sun_data['data'][0]

                # Check for sunrise and sunset times in the data
                if 'sunrise_ts' in first_day_data and 'sunset_ts' in first_day_data:

                    # Convert Unix timestamps to local time and format
                    tz = pytz.timezone('America/Los_Angeles')
                    sunrise = datetime.fromtimestamp(first_day_data['sunrise_ts'], tz=timezone.utc).astimezone(
                        tz).strftime('%I:%M %p').lstrip('0')
                    sunset = datetime.fromtimestamp(first_day_data['sunset_ts'], tz=timezone.utc).astimezone(
                        tz).strftime('%I:%M %p').lstrip('0')

                    # Create the tweet text
                    tweet_text = f"🌄 Sunrise at {sunrise}\n🌅 Sunset at {sunset}"
                    return tweet_text
                else:
                    return self.failure_text
            else:

                return response.status_code
        else:
            print(response.status_code)
            return self.failure_text

    def tweet_weather(self):
        tweet_text = self.fetch_weather()
        if self.validate_tweet(tweet_text):
            self.create_tweet(tweet_text)

    def tweet_weekly_forecast(self):
        tweet_text = self.fetch_weekly_forecast()
        if self.validate_tweet(tweet_text):
            self.create_tweet(tweet_text)

    def tweet_sun_times(self):
        tweet_text = self.fetch_sun_times()
        if self.validate_tweet(tweet_text):
            self.create_tweet(tweet_text)

    def print_calls(self, weatherful):
        '''

        Test all functions to ensure that they are working as expected 

        Returns:
            - Nothing

        '''
        weatherful_text = weatherful.fetch_weather()
        print(weatherful_text)
        print("--------------------------------------------")

        weatherful_text = weatherful.fetch_weekly_forecast()
        print(weatherful_text)
        print("--------------------------------------------")
        weatherful_text = weatherful.fetch_sun_times()

        print(weatherful_text)
        print("--------------------------------------------")
