import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv","r") as csvfile:
    tips = pd.read_csv(csvfile, delimiter=",")
    
tips_pivoted = tips.pivot_table(
    values = "tip",
    index = ["size"],
    columns = ["time"]
)

fig = sns.heatmap(tips_pivoted, annot=True, cmap="YlGn")
fig.set_ylim(0,6)

plt.xlabel("Tip")
plt.ylabel("Party Size")
plt.title("Party Size vs Average Tip Received")

plt.savefig("tips_vs_partysize.png")
    