# MM - Function

def my_function(stock1, stock2, stock3):
    print("The stocks used in this project are " + stock1 + ", " + stock2 + " & " + stock3 + ".")


my_function(stock1="Google", stock2="Gamestop", stock3="Amazon")

# MM - API Google

import requests

request = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=GOOGL&apikey=14U3Q94HL8MOK1IT")

print(request.status_code)

print(request.text)

# MM - API Gamestop

request = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=GME&apikey=14U3Q94HL8MOK1IT")

print(request.status_code)

print(request.text)

# MM - API Amazon

request = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=AMZN&apikey=14U3Q94HL8MOK1IT")

print(request.status_code)

print(request.text)

# MM - importing .csv dataframes

import pandas as pd

df = pd.read_csv("GOOG.csv")
df1 = pd.read_csv("GME_stock.csv")
df2 = pd.read_csv("Amazon.csv")

