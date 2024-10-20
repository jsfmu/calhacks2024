import tweepy
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Now you can access the variables from the .env file
api_key = os.getenv('TWITTER_API_KEY')
api_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_secret = os.getenv('TWITTER_ACCESS_SECRET')

class SocialMediaPost:
    def __init__(self, text, location, timestamp):
        self.text = text
        self.location = location
        self.timestamp = timestamp

class SocialMediaService:
    def __init__(self, seed_phrase):
        # Use environment variables to securely store Twitter API credentials
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_SECRET')

        # Authenticate using Tweepy
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def analyze_social_media(self, keywords, start_date=None, end_date=None):
        results = []
        
        # Search tweets based on the keywords
        query = ' OR '.join(keywords)
        tweets = self.api.search(q=query, count=100, lang='en', result_type='recent')

        for tweet in tweets:
            # Only include tweets with geolocation data
            if tweet.geo:
                post = SocialMediaPost(
                    text=tweet.text,
                    location=tweet.geo,
                    timestamp=str(tweet.created_at)
                )
                results.append(post)

        return results