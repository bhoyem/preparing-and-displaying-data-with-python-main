import matplotlib.pyplot as plt

snack_scores = [80,45,34]
colors = ["#DC143C", "#6495ED", "#7FFF00" ]

slice_labels = ["Chocolate", "Cheese", "Pickles"]

plt.pie(snack_scores, labels=slice_labels, colors=colors)

plt.title("Snack Scores", fontsize=30)

plt.savefig("snack_scores.png")