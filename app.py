import tweepy
from configparser import ConfigParser

config = ConfigParser()

class TwitterScrapper:
    def __init__(self, config_file):
        self.read_config(config_file)

    def read_config(self, config_file):
        if str(config_file).endswith('.ini'):
            config.read(config_file)

            api_key = config['Twitter']['api_key']
            api_secret = config['Twitter']['api_secret']
            access_token = config['Twitter']['access_token']
            access_secret = config['Twitter']['access_secret']

            return api_key, api_secret, access_token, access_secret

