from WeatherfulBot import WeatherfulBot
from TwitterClient import TwitterClient


class MainProgram:
    def __init__(self):
        self.weatherful = WeatherfulBot()

    def delete_tweets(self):
        twitter_client = TwitterClient(
            bearer_token='your_bearer_token',
            c_key='your_consumer_key',
            c_secret='your_consumer_secret',
            a_token='your_access_token',
            a_secret='your_access_token_secret'
        )
        twitter_client.delete_all_tweets()

    def run(self, type):
        if type == 'hourly':
            self.weatherful.tweet('hourly')
        elif type == 'weekly':
            self.weatherful.tweet('weekly')
        elif type == 'sun':
            self.weatherful.tweet('sun')
        return


if __name__ == "__main__":
    program = MainProgram()
    program.delete_tweets()  # This will delete all tweets
