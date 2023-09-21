import unittest
import tweepy
import requests
import json
import os
import schedule
import pytz 

from datetime import datetime, timezone
from time import sleep
from dotenv import load_dotenv
from unittest.mock import Mock, patch
from weatherful_bot import WeatherfulBot  # Make sure to import your WeatherfulBot class properly

class TestWeatherfulBot(unittest.TestCase):

    def setUp(self):
        self.bot = WeatherfulBot()
        
    @patch('requests.get')
    def test_fetch_weather(self, mock_get):
        # Mock data for fetch_weather
        mock_response_data = {
            'data': [{
                'temp': 75,
                'weather': {'description': 'clear sky'},
                'wind_spd': 5,
                'rh': 60,
                'uv': 1
            }]
        }
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response_data
        mock_get.return_value.text = json.dumps(mock_response_data)  # Add this line

        self.assertEqual(
        self.bot.fetch_weather(),
          "Hey Fullerton, it's currently 75°F with clear sky skies! \n🌬️The current Wind Speeds are: 5 mph \n💧 We are at 60%\n🌞 UV Index: 1\nStay comfy and safe! 😊"
        )     
        
    @patch('requests.get')
    def test_tweet_weekly_forecast(self, mock_get):
        mock_response_data = {
            "data": [
                {
                    "valid_date": "2023-01-01",
                    "high_temp": 75,
                    "low_temp": 55,
                    "weather": {"description": "clear sky"}
                },
                # Add more days if needed
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        self.assertEqual(
            self.bot.tweet_weekly_forecast(),
            "📅 7-day forecast for Fullerton:\n01-01: 75/55°F, clear sky"
        )

    @patch('requests.get')
    def test_tweet_sun_times(self, mock_get):
        # Mock data for sunrise and sunset
        mock_response_data = {
            "data": [{
                "sunrise_ts": 1677855510,  # Replace with appropriate Unix timestamps
                "sunset_ts": 1677898710
            }]
        }
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data
        
        tz = pytz.timezone('America/Los_Angeles')  # Use the appropriate time zone
        sunrise_expected = datetime.fromtimestamp(1677855510, tz=timezone.utc).astimezone(tz).strftime('%I:%M %p').lstrip('0')
        sunset_expected = datetime.fromtimestamp(1677898710, tz=timezone.utc).astimezone(tz).strftime('%I:%M %p').lstrip('0')
        
        expected_tweet_text = f"🌄 Sunrise at {sunrise_expected}\n🌅 Sunset at {sunset_expected}"

        self.assertEqual(self.bot.tweet_sun_times(), expected_tweet_text)

if __name__ == '__main__':
    unittest.main()
