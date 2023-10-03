import requests
import json
import pytz
from datetime import datetime, timezone
import logging


class WeatherClient:
    def __init__(self, city, weather_api):
        self.city = city
        self.weather_api = weather_api

        self.weather_comments = {
            "Clear sky": "it's the perfect day to go out! 🌞",
            "Few clouds": "it's a tad cloudy, but nice! 🌤",
            "Scattered clouds": "the clouds are playing hide and seek! ☁️🌤",
            "Broken clouds": "there are clouds everywhere, but it's cool! ⛅",
            "Shower rain": "uh oh! We've got rain, bring out those umbrellas! ☔",
            "Rain": "it's pouring rain! Stay cozy indoors. ☔🌧",
            "Thunderstorm": "we've got a thunderstorm! Stay safe indoors! ⛈",
            "Snow": "is that snow? We have a snow day! ☃️❄️",
            "Mist": "it's a little misty out! Stay safe. 🌫"
        }
        
        self.weekly_comments = { 
            "Clear sky": "it will be the perfect day to go out! 🌞",
            "Few clouds": "it will be a tad cloudy, but nice! 🌤",
            "Scattered clouds": "the clouds will be playing hide and seek! ☁️🌤",
            "Broken clouds": "there will be clouds everywhere, but it will be cool! ⛅",
            "Shower rain": "uh oh! We will have rain, bring out those umbrellas! ☔",
            "Rain": "it will be pouring rain! Stay cozy indoors. ☔🌧",
            "Thunderstorm": "we will have a thunderstorm! Stay safe indoors! ⛈",
            "Snow": "is that snow? We will have a snow day! ☃️❄️",
            "Mist": "it will be a little misty out! Stay safe. 🌫"
            }
        self.failure_text = "😢 Oops! Couldn't fetch the weather data. Stay tuned for updates! 🌧️"

        logging.basicConfig(level=logging.INFO)

    def _make_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.RequestException as e:
            logging.error(f"API Error: {e}")
            return None

    def fetch_weather(self):
        url = f"https://api.weatherbit.io/v2.0/current?&city={self.city}&key={self.weather_api}&units=I"
        data = self._make_request(url)

        if not data:
            return self.failure_text

        temp = data['data'][0]['temp']
        description = data['data'][0]['weather']['description']
        wind_speed = data['data'][0]['wind_spd']
        humidity = data['data'][0]['rh']
        uv_index = data['data'][0]['uv']
        comment = self.weather_comments.get(description, "Enjoy the day!")

        return f"Hey Fullerton, {comment}\n🌡️It's currently {temp}°F! \n🌬️The current Wind Speeds are: {wind_speed} mph\
            \n💧 We are at {humidity}% humidity\n🌞ay comfy and safe! 😊\
            \n#Fullerton #CSUF #FullertonWeather"

    def fetch_sun_times(self):
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={self.city}&key={self.weather_api}&units=I"
        response = requests.get(url)

        if response.status_code == 200:
            sun_data = json.loads(response.text)

            if 'data' in sun_data and sun_data['data']:
                first_day_data = sun_data['data'][0]

                if 'sunrise_ts' in first_day_data and 'sunset_ts' in first_day_data:

                    tz = pytz.timezone('America/Los_Angeles')
                    sunrise = datetime.fromtimestamp(first_day_data['sunrise_ts'], tz=timezone.utc).astimezone(
                        tz).strftime('%I:%M %p').lstrip('0')
                    sunset = datetime.fromtimestamp(first_day_data['sunset_ts'], tz=timezone.utc).astimezone(
                        tz).strftime('%I:%M %p').lstrip('0')

                    tweet_text = f"Hello Fullerton!\nToday the sun will rise at {sunrise}🌄 and set at {sunset}🌅\n Have a great day!🌞"
                    return tweet_text + '\n#Fullerton #FullertonWeather #CSUF #CSUFWeather #Sunrise #Sunset'
                else:
                    return self.failure_text
            else:

                return response.status_code
        else:
            print(response.status_code)
            return self.failure_text

    def fetch_weekly_forecast(self):
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={self.city}&key={self.weather_api}&units=I&days=7"
        response = requests.get(url)

        if response.status_code == 200:
            forecast_data = json.loads(response.text)
            tweet_text = "🛰️☁️ 7-day forecast for Fullerton:"
            
            # Dictionary to group days by their description
            grouped_days = {}
            for day in forecast_data['data']:
                full_date = day['valid_date']
                date_obj = datetime.strptime(full_date, "%Y-%m-%d")
                day_of_week = date_obj.strftime("%a")
                max_temp = int(day['high_temp'])
                min_temp = int(day['low_temp'])
                description = day['weather']['description']
                
                if description not in grouped_days:
                    grouped_days[description] = []
                grouped_days[description].append(f"{day_of_week} | {max_temp}/{min_temp}°F🌡️")
                
            # Append grouped days to the tweet_text
            for desc, days_list in grouped_days.items():
                for day_info in days_list:
                    tweet_text += f"\\n{day_info}"
                comment = self.weekly_comments.get(desc, "Enjoy the day!")
                tweet_text += f"\\nDescription: {comment}\\n"
            
            return tweet_text
        else:
            error_message = f"Failed to fetch forecast. Error: {response.status_code}"
            print(error_message)
            return error_message

