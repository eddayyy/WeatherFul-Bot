import tweepy
import requests
import json
import os
import schedule
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

        self.client = tweepy.Client(
            self.bearer_token, c_key, c_secret, a_token, a_secret)
        self.auth = tweepy.OAuth1UserHandler(
            c_key, c_secret, a_token, a_secret)
        self.api = tweepy.API(self.auth)

    def validate_tweet(self, tweet_text):
        if len(tweet_text) > 280:
            return False
        return True

    def create_tweet(self, text):
        self.client.create_tweet(text=text)

    def fetch_weather(self):
        lat = "33.8704"
        lon = "-117.9243"
        url = f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={self.weather_api}&units=I"

        response = requests.get(url)

        if response.status_code == 200:
            weather_data = json.loads(response.text)
            temp = weather_data['data'][0]['temp']
            description = weather_data['data'][0]['weather']['description']
            wind_speed = weather_data['data'][0]['wind_spd']
            humidity = weather_data['data'][0]['rh']
            uv_index = weather_data['data'][0]['uv']

            return f"Hey Fullerton, it's currently {temp}°F with {description} skies! \n🌬️The current Wind Speeds are: {wind_speed} mph \n💧 We are at {humidity}%\n🌞 UV Index: {uv_index}\nStay comfy and safe! 😊"
        else:
            return "😢 Oops! Couldn't fetch the weather data. Stay tuned for updates! 🌧️"

    def tweet_weekly_forecast(self):
        lat = "33.8704"
        lon = "-117.9243"
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lon}&key={self.weather_api}&units=I&days=7"

        response = requests.get(url)

        if response.status_code == 200:
            forecast_data = json.loads(response.text)
            tweet_text = "📅 7-day forecast for Fullerton:"

            for day in forecast_data['data']:
                date = day['valid_date'][5:]  # Omit year (keep only month-day)
                max_temp = int(day['high_temp'])  # Convert to integer
                min_temp = int(day['low_temp'])  # Convert to integer
                description = day['weather']['description']

                # Abbreviate to reduce text length
                new_line = f"\n{date}: {max_temp}/{min_temp}°F, {description}"

                # Check if the tweet is getting too long
                if len(tweet_text + new_line) > 280:
                    break

                tweet_text += new_line

            return tweet_text
        else:
            return "😢 Oops! Couldn't fetch the weather data. Stay tuned for updates! 🌧️"

    def tweet_sun_times(self):
        lat = "33.8704"
        lon = "-117.9243"
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lon}&key={self.weather_api}&units=I"

        response = requests.get(url)

        if response.status_code == 200:
            sun_data = json.loads(response.text)
            sunrise = sun_data['data'][0]['sunrise']
            sunset = sun_data['data'][0]['sunset']

            tweet_text = f"🌄 Sunrise at {sunrise}\n🌅 Sunset at {sunset}"

            return tweet_text
        else:
            return "😢 Oops! Couldn't fetch the weather data. Stay tuned for updates! 🌧️"


if __name__ == "__main__":
    weatherful = WeatherfulBot()

    # Instantly run each function for debugging
    # weather_status = weatherful.fetch_weather()
    # if weather_status:
    #     weatherful.create_tweet(weather_status)

    weather_status = weatherful.tweet_weekly_forecast()
    if weather_status and weatherful.validate_tweet(weather_status):
        weatherful.create_tweet(weather_status)
    else:
        print("Tweet is too long.")

    # weather_status = weatherful.tweet_sun_times()
    # if weather_status:
    #     weatherful.create_tweet(weather_status)

    # Then continue with your scheduled tasks
    # schedule.every().hour.do(weatherful.fetch_weather)
    # schedule.every().sunday.at("12:00").do(weatherful.tweet_weekly_forecast)
    # schedule.every().day.at("06:00").do(weatherful.tweet_sun_times)
    # schedule.every().day.at("18:00").do(weatherful.tweet_sun_times)

    # while True:
    #     schedule.run_pending()
    #     sleep(1)
