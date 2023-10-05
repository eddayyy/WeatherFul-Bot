from WeatherfulBot import WeatherfulBot


class MainProgram:
    def __init__(self):
        self.weatherful = WeatherfulBot()

    def run(self, type):
        if type == 'hourly':
            self.weatherful.tweet('hourly')
        elif type == 'weekly':
            self.weatherful.tweet('weekly')
        elif type == 'sun':
            self.weatherful.tweet('sun')
        return
