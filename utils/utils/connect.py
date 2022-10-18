# For connecting to api-football api
# https://v3.football.api-sports.io/{endpoint}

import requests

url = 'https://v3.football.api-sports.io/fixtures/rounds?season=2019&league=61'

payload = {}
headers = {
        'x-rapidapi-key': "a3563512ec8e2381f541fb2d0ca49a84",
        'x-rapidapi-host': "v3.football.api-sports.io"
        
        }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
