
import matplotlib.pyplot as plt
import pandas as pd

def plot_trophy_history(csv_file):
    df = pd.read_csv(csv_file)
    df = df.dropna(how="all")

    plt.plot(df["timestamp"], df["trophies"])
    plt.xlabel("Date")
    plt.ylabel("Trophies")
    plt.title(f"Trophy History for {df["name"].iloc[0]}")

    plt.show()

plot_trophy_history("player_data/V2PV9LGUV.csv")