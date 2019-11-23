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

