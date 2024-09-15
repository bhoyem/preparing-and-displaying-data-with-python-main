import csv
import numpy as np

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

size = data_numpy[:,6]
tips = np.array(data_numpy[:,1], dtype=float)
bills = np.array(data_numpy[:,0], dtype=float)
tip_percentages = tips/bills

print(f"The average bill is: ${np.mean(bills).round(2)}")
print(f"The median bill is: ${np.median(bills).round(2)}")
print(f"The minimum bill is: ${np.min(bills).round(2)}")
print(f"The maximum bill is: ${np.max(bills).round(2)}")