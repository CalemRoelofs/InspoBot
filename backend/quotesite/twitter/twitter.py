import tweepy

from django.conf import settings


auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
auth.set_access_token(
    settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

tweet_text = "#inspirational #quote #inspodaily"
