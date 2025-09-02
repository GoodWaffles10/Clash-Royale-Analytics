
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

api_token = config["api_token"]
player_tag = config["player_tag"]


def fetch_player_data():
    url = f"https://api.clashroyale.com/v1/players/%23{player_tag}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    data = response.json()

    return {
        "name": data["name"],
        "tag": data["tag"],
        "trophies": data["trophies"],
        "wins": data["wins"],
        "losses": data["losses"],
        "battleCount": data["battleCount"],
        "trophies": data["trophies"],
        "progress": data["progress"],
    }

def fetch_battlelog():
    url = f"https://api.clashroyale.com/v1/players/%23{player_tag}/battlelog"
    headers = { "Authorization": f"Bearer {api_token}" }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    data = response.json()[0]

    return {
        "opponent_tag": data["opponent"][0]["tag"],
        "opponent_name": data["opponent"][0]["name"]
    }

