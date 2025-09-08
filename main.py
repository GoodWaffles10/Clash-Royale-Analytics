
import os
from datetime import datetime
import pandas as pd
from player import Player
import plotting

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

    folder_name = player.player_tag.lstrip("#")
    player_folder = os.path.join("player_data", folder_name)

    if not os.path.exists(player_folder):
        os.makedirs(player_folder)

    csv_file = os.path.join(player_folder, f"{folder_name}.csv")
    
    try:
        df_existing = pd.read_csv(csv_file)
        df = pd.concat([df_existing, df], ignore_index=True)
    except FileNotFoundError:
        pass
    
    def remove_dupes(path):
        if os.path.exists(path):
            os.remove(path)
    
    remove_dupes(os.path.join(player_folder, f"{folder_name}_trophy_history_days.png"))
    remove_dupes(os.path.join(player_folder, f"{folder_name}_over_all_battles.png"))
    remove_dupes(os.path.join(player_folder, f"{folder_name}_trophy_history_past_week.png"))
    plotting.plot_trophy_history_over_days(csv_file, os.path.join(player_folder, f"{folder_name}_trophy_history_days.png"))
    plotting.plot_trophy_history_over_battles(csv_file, os.path.join(player_folder, f"{folder_name}_over_all_battles.png"))
    plotting.plot_trophy_history_past_week(csv_file, os.path.join(player_folder, f"{folder_name}_trophy_history_past_week.png"))

    df.to_csv(csv_file, index=False)
    
    
    print(f"Data for player {player.player_tag} saved to {csv_file}")


