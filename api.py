
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

api_token = config["api_token"]

def fetch_player_data(player_tag):
    url = f"https://api.clashroyale.com/v1/players/%23{player_tag}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    return response.json()



def fetch_battlelog(player_tag):
    url = f"https://api.clashroyale.com/v1/players/%23{player_tag}/battlelog"
    headers = { "Authorization": f"Bearer {api_token}" }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    return response.json()[0]

