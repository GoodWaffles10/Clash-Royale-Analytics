
from datetime import datetime
import pandas as pd

from api import fetch_player_data, fetch_battlelog

player_data = fetch_player_data()
battlelog = fetch_battlelog()

if player_data is None:
    print("failed to fetch player data, exiting")
    exit()
if battlelog is None:
    print("failed to fetch battlelog, exiting")
    exit()

player_row = {
    "timestamp": datetime.now().isoformat(),
    "name": player_data["name"],
    "tag": player_data["tag"],
    "trophies": player_data["trophies"],
    "wins": player_data["wins"],
    "losses": player_data["losses"],
    "battleCount": player_data["battleCount"],
}

# wrap in DataFrame for concatenation
player_row_df = pd.DataFrame([player_row])

# Try to load CSV; if it fails, create new DataFrame
try:
    df_player = pd.read_csv("player_data.csv")
    df_player = pd.concat([df_player, player_row_df], ignore_index=True)
except FileNotFoundError:
    df_player = player_row_df

# save to csv
df_player.to_csv("player_data.csv", index=False)

# after saving to csv, open in excel, google sheets, or vsc csv viewer
print(df_player)