# For connecting to api-football api
# https://v3.football.api-sports.io/{endpoint}
# current code only works for 2019 league 61 and fixtures
# plan on make this able to accept multiple different endpoints

import requests

url = 'https://v3.football.api-sports.io/fixtures/rounds?season=2019&league=61'

def api_connect(API_KEY):
    payload = {}
    headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "v3.football.api-sports.io" 
            }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response
