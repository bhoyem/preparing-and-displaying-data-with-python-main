import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

with open("books.csv","r", encoding="utf-8") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

fig = sns.scatterplot(
    x="# num_pages", 
    y="average_rating", 
    hue="average_rating", 
    size="# num_pages", 
    sizes=(20,350), 
    data=data, 
    palette="blend:#E55648,#50B131",
    legend="auto")

plt.title("Book Avg Ratings vs Page Count")
plt.xlabel("Number of Pages")
plt.ylabel("Average Rating")

plt.savefig("avg-book-ratings.png")
# print(data["language_code"])

