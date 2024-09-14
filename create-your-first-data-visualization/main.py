# Import matplotlib library here
import matplotlib.pyplot as plt

# Let's rank some of our favorite snacks
snack_scores = [85, 40, 90]
slice_labels = ["chips", "nuts", "cheese puffs"]


# Let's make a pie chart!
plt.pie(snack_scores, labels=slice_labels)

# Give your pie chart a title in the quotes
plt.title("Bryan's Favorite Snacks")

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("bryans_snacks")