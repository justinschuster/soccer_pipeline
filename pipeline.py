import config

from utils.utils import connect
from utils.utils.helpers import leagues

# Testing the api key connect
live_fixtures = connect.get_live_fixtures(config.API_KEY)
print(live_fixtures.text)

