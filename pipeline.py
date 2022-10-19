import config

from utils.utils import connect
from utils.utils.helpers import leagues

# Testing the api key connect
print('English Premier League')
fixtures_EPL = connect.get_todays_fixtures(config.API_KEY, leagues.codes['English Premier League'])
print(fixtures_EPL.text)
print('\n----------------\n')
print('UEFA Champions League')
fixtures_UCL = connect.get_todays_fixtures(config.API_KEY, leagues.codes['UEFA Champions League'])
print(fixtures_UCL.text)
