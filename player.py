
from datetime import datetime
import pandas as pd
from api import fetch_player_data, fetch_battlelog

class Player:
    def __init__(self, player_tag):
        self.player_tag = player_tag
        self.player_data = {} # holds current snapshot

    def filter_player_data(self):
        raw = fetch_player_data(self.player_tag)
        if raw is None:
            print("failed to fetch player_data")
            return None

        self.player_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "name": raw["name"],
            "player_tag": raw["tag"],
            "trophies": raw["trophies"],
            "bestTrophies": raw["bestTrophies"],
            "wins": raw["wins"],
            "losses": raw["losses"],
            "battleCount": raw["battleCount"],
        } 

        return self.player_data

    
    def filter_battlelog(self):
        self.battlelog_data = fetch_battlelog(self.player_tag)
        if self.battlelog_data is None:
            print("failed to fetch battlelog")
            return None
        
        return {
            "opponent_tag": self.battlelog_data["opponent"][0]["tag"],
            "opponent_name": self.battlelog_data["opponent"][0]["name"]
        }
        pass  # Implement if needed
    
    # convert player_data to player_dataframe
    def to_player_dataframe(self):
        return pd.DataFrame([self.player_data])