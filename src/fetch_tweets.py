import os
import tweepy as tw
import pandas as pd 
import yaml

with open(r'../API-Info.yaml') as file:
    config = yaml.full_load(file)
    

consumer_key = config["APIKey"]
consumer_secret = config["APISecret"]
access_token = config["AccessToken"]
access_token_secret = config["AccessTokenSecret"]

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#Trump"
date_since = "2019-11-20"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
print([tweet.text for tweet in tweets])