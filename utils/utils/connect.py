# For connecting to api-football api
# https://v3.football.api-sports.io/{endpoint}
# current code only works for 2019 league 61 and fixtures
# plan on make this able to accept multiple different endpoints
# NEED BETTER WAY TO ACCESS API_KEY

import requests

from datetime import date

url = 'https://v3.football.api-sports.io'

def api_call(API_KEY, url):  
    payload = {}
    headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "v3.football.api-sports.io" 
            }  

    response = None
    while True:
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            break
        except ValueError:
            print('Oops that request didn\'t work')

    if (response.status_code != 200):
        print(f'Unsuccesful request. Status code: {response.status_code}')
    else:
        return response

def get_todays_fixtures(API_KEY, league):
    # TODO: response status returns succesfull even if league or year doesn't yield results
    # Need to program a check for that
    # need to get list of season and league id's

    current_year = date.today().year
    new_url = url + f'/fixtures/rounds?season={current_year}&league=4335'
    
    response = api_call(API_KEY, new_url)
    if response is not None:
        return response
