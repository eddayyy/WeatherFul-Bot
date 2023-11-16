import requests
import json
import pytz
import logging

from datetime import datetime, timezone


class WeatherClient:
    def __init__(self, city, weather_api):
        self.city = city
        self.weather_api = weather_api

        self.weather_comments = {
            # All possible descriptions to be returned by weatherbits API, these comments are meant to elevate tweets and make them more compelling.
            "Clear sky": "it's the perfect day to go out! 🌞",
            "Few clouds": "it's a bit cloudy at the moment! 🌤",
            "Scattered clouds": "the clouds are playing hide and seek! ☁️🌤",
            "Broken clouds": "there are clouds everywhere, but it's cool! ⛅",
            "Shower rain": "uh oh! We've got rain, bring out those umbrellas! ☔",
            "Rain": "it's pouring rain! Stay cozy indoors. ☔🌧",
            "Drizzle": "it's drizzling! Stay cozy indoors. ☔🌧",
            "Overcast Clouds": "it's pouring rain! Stay cozy indoors. ☔🌧",
            "Thunderstorm": "we've got a thunderstorm! Stay safe indoors! ⛈",
            "Snow": "is that snow? We have a snow day! ☃️❄️",
            "Mist": "it's a little misty out! Stay safe. 🌫",
            "Thunderstorm with light rain": "there's a light thunderstorm! Be cautious! ⛈🌦",
            "Thunderstorm with rain": "there's a thunderstorm with rain, stay indoors! ⛈🌧",
            "Thunderstorm with heavy rain": "there's a heavy thunderstorm alert! Stay safe! ⛈🌧",
            "Thunderstorm with light drizzle": "we have a light drizzly thunderstorm! Stay dry! ⛈🌦",
            "Thunderstorm with drizzle": "there's a drizzly thunderstorm outside! ⛈🌦",
            "Thunderstorm with heavy drizzle": "there's currently a heavy drizzle and thunderstorm! ⛈🌦",
            "Thunderstorm with Hail": "it's currently hailing along with a thunderstorm! Be very cautious! ⛈❄️",
            "Light Drizzle": "there's a bit of drizzle out there! 🌦",
            "Heavy Drizzle": "we should expect heavy drizzle! Stay dry! 🌦",
            "Light Rain": "we've got light rain, might need an umbrella! ☔",
            "Moderate Rain": "there's moderate rain outside, stay dry! ☔",
            "Heavy Rain": "heavy rain alert! Stay indoors and dry! ☔🌧",
            "Freezing rain": "beware of freezing rain! Stay warm! ☔❄️",
            "Light shower rain": "light showers are expected, carry an umbrella! ☔",
            "Heavy shower rain": "heavy showers ahead! Stay dry! ☔🌧",
            "Light snow": "light snow flurries! Enjoy the snow! ☃️❄️",
            "Snow": "snowfall alert! Stay warm and safe! ☃️❄️",
            "Heavy Snow": "heavy snow expected! Bundle up! ☃️❄️",
            "Mix snow/rain": "mixed snow and rain! Dress warmly! ☔❄️",
            "Sleet": "sleet ahead, be cautious on roads! ❄️☔",
            "Heavy sleet": "heavy sleet, watch your step! ❄️☔",
            "Snow shower": "snow showers incoming! Enjoy the view! ☃️❄️",
            "Heavy snow shower": "heavy snow showers! Stay warm! ☃️❄️",
            "Flurries": "flurries in the air! Enjoy the snow! ☃️❄️",
            "Mist": "misty conditions, drive safely! 🌫",
            "Smoke": "smoky conditions, take care! 🌫",
            "Haze": "hazy weather, be cautious! 🌫",
            "Sand/dust": "sandy or dusty, protect your eyes! 🌫",
            "Fog": "foggy weather, drive safely! 🌫",
            "Freezing Fog": "freezing fog around, stay warm! 🌫❄️",
            "Unknown Precipitation": "unknown precipitation, be prepared for anything! ☔❄️",
            "Overcast clouds": "we've got overcast skies, it's getting gloomy! ☁️",
            "Unknown Precipitation": "unpredictable weather ahead! Stay prepared! ☔❄️"
        }

        self.weekly_comments = {
            "Clear Sky": "\n🌞 Nothing but clear skies on:",
            "Cloudy": "\n⛅ There will be clouds everywhere, but it'll be fresh on:",
            "Rain": "\n☔🌧 Bring out those umbrellas! It will be raining on:",
            "Thunderstorm": "\n⛈ Theres a thunderstorm on the way! Stay safe indoors on:",
            "Snow": "\n☃️❄️ Snow is on the way! Be prepared for it to snow on:",
        }

        self.failure_text = "😢 Oops! Couldn't fetch the weather data. Stay tuned for updates! 🌧️"

        logging.basicConfig(level=logging.INFO)

    def fetch_weather(self):
        url = f"https://api.weatherbit.io/v2.0/current?&city={self.city}&key={self.weather_api}&units=I"
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            temp = data['data'][0]['temp']
            description = data['data'][0]['weather']['description']
            wind_speed = data['data'][0]['wind_spd']
            humidity = data['data'][0]['rh']
            comment = self.weather_comments.get(description, "Enjoy the day!")

            return f"Hey Fullerton, {comment}\n🌡️It's currently {temp}°F! \n🌬️The current Wind Speeds are: {wind_speed} mph\
                \n💧 We are at {humidity}% humidity\n🌞Stay comfy and safe! 😊\
                \n#Fullerton #CSUF #FullertonWeather"
        else:
            return self.failure_text

    def fetch_sun_times(self):
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={self.city}&key={self.weather_api}&units=I"
        response = requests.get(url)

        if response.status_code == 200:
            sun_data = json.loads(response.text)
            first_day_data = sun_data['data'][0]

            tz = pytz.timezone('America/Los_Angeles')
            sunrise = datetime.fromtimestamp(first_day_data['sunrise_ts'], tz=timezone.utc).astimezone(
                tz).strftime('%I:%M %p').lstrip('0')
            sunset = datetime.fromtimestamp(first_day_data['sunset_ts'], tz=timezone.utc).astimezone(
                tz).strftime('%I:%M %p').lstrip('0')

            tweet_text = f"Good Morning Fullerton!☀️\nThe sun will rise at {sunrise}🌅 and set at {sunset}🌇\n Have a great day!🌞"
            return tweet_text + '\n#CSUF #Fullerton  #FullertonWeather  #Sunrise #Sunset'
        else:
            return self.failure_text

    def fetch_weekly_forecast(self):
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={self.city}&key={self.weather_api}&units=I&days=8"
        response = requests.get(url)

        if response.status_code == 200:
            forecast_data = json.loads(response.text)
            tweet_text = "🛰️☁️ 7-day forecast for Fullerton:\n"

            # Dictionary to group days by their description
            grouped_days = {}
            for day in forecast_data['data'][1::]:

                full_date = day['valid_date']
                date_obj = datetime.strptime(full_date, "%Y-%m-%d")
                day_of_week = date_obj.strftime("%a")
                max_temp = int(day['high_temp'])
                min_temp = int(day['low_temp'])
                description = day['weather']['description']

                if description in ('Shower rain', 'Rain', 'Mist'):
                    description = 'Rain'
                elif description in ('Few clouds', 'Scattered clouds', 'Broken clouds'):
                    description = 'Cloudy'
                if description not in grouped_days:
                    grouped_days[description] = []

                grouped_days[description].append(
                    f"📆{day_of_week} | {max_temp}/{min_temp}°F🌡️")

            # Append grouped days to the tweet_text
            for desc, days_list in grouped_days.items():
                comment = self.weekly_comments.get(desc, '')
                tweet_text += f"\n{comment}"
                for day_info in days_list:
                    tweet_text += f"\n{day_info}"
            return tweet_text.strip()
        else:
            return self.failure_text
