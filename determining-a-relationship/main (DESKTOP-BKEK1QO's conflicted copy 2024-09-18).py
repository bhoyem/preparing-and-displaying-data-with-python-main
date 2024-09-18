import requests
import pandas as pd


# Standardizes currency to USD values so that we can better compare results
def format_currency(dataset):
  url = "https://api.exchangerate-api.com/v4/latest/USD"

  # Requests data from API
  response = requests.get(url)
  data = response.json()

  def convert_currency(row):
    rate = data["rates"][row["Unit Code"]]
    return row["Value"] / rate

  for index, row in dataset.iterrows():
    dataset.at[index, "Unit Code"] = "USD"
    dataset.at[index, "Value"] = convert_currency(row)
  return dataset


# ADD CODE: Pandas dataframes
wage = pd.read_csv("wage.csv", delimiter=",")
# print(wage)
happiness = pd.read_csv("happiness.csv", delimiter=",")
print(f"Happiness: \n{happiness}")

wage_usd = format_currency(wage)
print(f"Wage: \n{wage_usd}")

wage_and_happiness = wage.merge(happiness)
print(f"Wage and happiness: \n{wage_and_happiness}")

wage_and_happiness_by_country = wage_and_happiness.groupby("Country")
print(f"Wage and happiness by Country: \n{wage_and_happiness}")
wage_average_per_country = wage_and_happiness_by_country["Value"].mean()
print(f"Wage average per Country: \n{wage_average_per_country}")
happiness_average_per_country = wage_and_happiness_by_country["Happiness score"].mean()
print(f"Happiness average per Country \n{happiness_average_per_country}")

print(f"Countries with the largest average wages: \n{wage_average_per_country.nlargest(10)}")
print(f"Countries with the lowest average wages: \n{wage_average_per_country.nsmallest(10)}")
print(f"Countries with the highest average happiness: \n{happiness_average_per_country.nlargest(10)}")
print(f"Countries with the lowest average happiness: \n{happiness_average_per_country.nsmallest(10)}")
