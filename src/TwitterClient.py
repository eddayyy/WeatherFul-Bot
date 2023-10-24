import tweepy
import logging


class TwitterClient:
    def __init__(self, bearer_token, c_key, c_secret, a_token, a_secret):
        self.client = tweepy.Client(
            bearer_token, c_key, c_secret, a_token, a_secret
        )
        self.auth = tweepy.OAuth1UserHandler(
            c_key, c_secret, a_token, a_secret
        )
        self.api = tweepy.API(self.auth)
        logging.basicConfig(level=logging.INFO)

    def create_tweet(self, text):
        try:
            self.client.create_tweet(text=text)
        except tweepy.TweepyException as e:
            print(e)
