from WeatherfulBot import WeatherfulBot


if __name__ == '__main__':
    weatherful = WeatherfulBot()
    weatherful.tweet('weekly')
    weatherful.tweet('hourly')
    weatherful.tweet('sun')
