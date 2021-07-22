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

# MM - Adding Unique Identifier Column

df.insert(1, "Company", "Google")
df1.insert(1, "Company", "Gamestop")
df2.insert(1, "Company", "Amazon")

# MM - sorting imported data

df['Date'] = pd.to_datetime(df.Date, infer_datetime_format=True)
df.sort_values(by='Date', ascending=False, inplace=True)
print(df)

df1['Date'] = pd.to_datetime(df1.Date, infer_datetime_format=True)
df1.sort_values(by='Date', ascending=False, inplace=True)
print(df1)

df2['Date'] = pd.to_datetime(df2.Date, infer_datetime_format=True)
df2.sort_values(by='Date', ascending=False, inplace=True)
print(df2)

# MM - merging csv's, first merge

df3 = df.append(df1, sort=False)
print(df3)

# MM - merging csv's, second merge

df4 = df3.append(df2, sort=False)
print(df4)

# MM - sorting merged file

df4['Date'] = pd.to_datetime(df.Date, infer_datetime_format=True)

# MM - Dropping rows with no date

df4.dropna(subset=['Date'], inplace=True)
print(df4)

# MM - iterrows/Indexing to Add Year column

import numpy as np

df4['Year'] = np.nan

for index, row in df4.iterrows():
    df4.loc[index, 'Year'] = df.loc[index, 'Date'].year

# MM - Data Cleansing

df4['Year'] = df4['Year'].astype(int).replace('\.0', '', regex=True)
df4['Volume'] = df4['Volume'].astype(int).replace('\.0', '', regex=True)
df4.Open = df4.Open.round(2)
df4.High = df4.High.round(2)
df4.Low = df4.Low.round(2)
df4.Close = df4.Close.round(2)
df4['Adj Close'] = df4['Adj Close'].round(2)