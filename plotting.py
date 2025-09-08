
import matplotlib.pyplot as plt
import pandas as pd

def plot_trophy_history_over_days(csv_file, save_path):
    df = pd.read_csv(csv_file)
    df = df.dropna(how="all")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    formatted_time = df["timestamp"].dt.strftime("%m/%d")

    plt.plot(formatted_time, df["trophies"])
    plt.xlabel("Date")
    plt.ylabel("Trophies")
    plt.title(f"Trophy History for {df["name"].iloc[0]}")

    plt.savefig(save_path)
    plt.close()

def plot_trophy_history_over_battles(csv_file, save_path):
    df = pd.read_csv(csv_file)
    df = df.dropna(how="all")

    #df["timestamp"] = pd.to_datetime(df["timestamp"])
    #formatted_time = df["timestamp"].dt.strftime("%m/%d")

    plt.plot(df["battleCount"], df["trophies"])
    plt.xlabel("battleCount")
    plt.ylabel("Trophies")
    plt.title(f"Trophy History for {df["name"].iloc[0]} over battles")

    plt.savefig(save_path)
    plt.close()

def plot_trophy_history_past_week(csv_file, save_path):
    df = pd.read_csv(csv_file).tail(7)
    df = df.dropna(how="all")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    formatted_time = df["timestamp"].dt.strftime("%m/%d")

    plt.plot(formatted_time, df["trophies"])
    plt.xlabel("Date")
    plt.ylabel("Trophies")
    plt.title(f"Trophy History for {df["name"].iloc[0]}")

    plt.savefig(save_path)
    plt.close()