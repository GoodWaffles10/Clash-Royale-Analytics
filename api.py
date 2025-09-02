
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
print(config["player_tag"])

api_token = config["api_token"]
player_tag = config["player_tag"]

if not player_tag.startswith("#"):
    player_tag = "#" + player_tag

def fetch_player_data(player_tag, api_token):
    url = f"https://api.clashroyale.com/v1/players/{player_tag}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    data = response.json()
    print(data)
    return {
        "name": data["name"],
        "trophies": data["trophies"],
        "wins": data["wins"],
        "losses": data["losses"],
        "battleCount": data["battleCount"],
        "trophies": data["trophies"],
        "progress": data["progress"]
    }

fetch_player_data(player_tag, api_token)