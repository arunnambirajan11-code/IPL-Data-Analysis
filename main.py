import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IPL.csv")

top_batters = df.groupby("batter")["runs_batter"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_batters.plot(kind="bar")
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Batter")
plt.ylabel("Runs")
plt.tight_layout()

plt.show()