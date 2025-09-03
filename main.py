
import os
from datetime import datetime
import pandas as pd
from player import Player

data_folder = "player_data"
os.makedirs(data_folder, exist_ok=True) # creates folder if it doesnt exist

# dont include hashtags in tags
players = [
    Player("J8J8QR8YU"),
    Player("LJ0RQCY8R"),
    Player("CJLYGCJ8G"),
    Player("U2282JYGL"),
    Player("V2PV9LGUV"),
]

for player in players:
    player.filter_player_data()
    df = player.to_player_dataframe()

    csv_file = os.path.join(data_folder, f"{player.player_tag}.csv")

    try:
        df_existing = pd.read_csv(csv_file)
        df = pd.concat([df_existing, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv(csv_file, index=False)

    print(f"Data for player {player.player_tag} saved to {csv_file}")
