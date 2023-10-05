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

    def validate_tweet(self, tweet_text):
        # Here you can add more sophisticated validation
        if len(tweet_text) <= 280:
            return True
        logging.warning("Tweet validation failed: Tweet is too long")
        return False

    def create_tweet(self, text, type):
        try:
            tweet = self.client.create_tweet(text=text)
            if type == 'weekly':
                self.pin_tweet(tweet)
        except tweepy.TweepyException as e:
            print(e)

    def pin_tweet(self, tweet_id):
        try:
            user_timeline = self.api.user_timeline(count=1)
            if user_timeline:
                # Unpin the current pinned tweet if there's any
                current_pinned_tweet = user_timeline[0]
                if current_pinned_tweet.pinned:
                    current_pinned_tweet.unpin()
            # Pin the new tweet
            tweet = self.api.get_status(tweet_id)
            # tweet.pin() Work in progress
        except tweepy.TweepyException as e:
            logging.error(f"Failed to pin tweet: {e}")
