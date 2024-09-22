import matplotlib.pyplot as plt
import pandas as pd
import re
import json
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic

classes = ["Mammalia", "Aves", "Reptilia"]
statuses = ["Endangered", "Critically endangered", "Vulnerable"]

mosaic_data = []

with open("data.json", "r") as text:
    data = json.load(text)

for item in data:
  item["Category"] = re.compile(" [\.(]").split(item["Category"])[0]

for item in data:
   if item["Animal Class"] in classes and item["Category"] in statuses:
      mosaic_data.append(item)

properties = {
   "Endangered": {"color": "#FACDB6"},
   "Critically endangered": {"color": "#C5CADE"},
   "Vulnerable": {"color": "#A8DBD2"}
}

plt.rc("font", size=8)

mosaic_dataframe = pd.DataFrame(mosaic_data)

fig = mosaic(
   mosaic_dataframe, 
   ["Category", "Animal Class"], 
   title="Conservation Status by Animal Class", 
   gap=[0.02, 0.02], 
   axes_label=True, 
   properties=lambda x: properties[x[0]])

plt.savefig("endangered-species-mosaic.png")



# print(data)