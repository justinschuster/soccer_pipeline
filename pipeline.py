import config

from utils.utils import connect

# Testing the api key connect
fixtures = connect.get_todays_fixtures(config.API_KEY)
