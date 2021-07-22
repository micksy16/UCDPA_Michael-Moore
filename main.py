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

# MM - Converting to Datetime

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

# MM - Creating Dictionaries for stock price @ 19th July 21

dfdict = {
    "Date": "2021-07-19",
    "Company": "Google",
    "Open": 2623.11,
    "High": 2624.94,
    "Low": 2570.74,
    "Close": 2577.75,
    "Adj Close": 2577.75,
    "Volume": 78878000,
}

df1dict = {
    "Date": "2021-07-19",
    "Company": "Gamestop",
    "Open": 164.30,
    "High": 174.22,
    "Low": 161.22,
    "Close": 172.09,
    "Adj Close": 172.09,
    "Volume": 4810000,
}

df2dict = {
    "Date": "2021-07-19",
    "Company": "Amazon",
    "Open": 3532.58,
    "High": 3534.00,
    "Low": 3522.55,
    "Close": 3531.51,
    "Adj Close": 3531.51,
    "Volume": 3580000,
}

# MM - converting Dictionaries to Panda Dataframes

dfjuly = pd.DataFrame.from_dict(dfdict, orient='index')

print(dfjuly)

df1july = pd.DataFrame.from_dict(df1dict, orient='index')

print(df1july)

df2july = pd.DataFrame.from_dict(df2dict, orient='index')

print(df2july)

# MM - Insights using loops/functions/matplotlib/grouping

# MM - Visual 1

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 8))

df4filt1 = df4[(df4.Date == '2019-12-31')]

plots = sns.barplot(x="Company", y="Adj Close", data=df4filt1)

for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')

plt.xlabel("Company", size=14)
plt.ylabel("Closing Share Price", size=14)
plt.title("2019 Year End Stock Price")
plt.show()

# MM - Visual 2

plt.figure(figsize=(8, 8))

df4filt2 = df4[(df4.Date == '2018-12-31')]

plots = sns.barplot(x="Company", y="Adj Close", data=df4filt2)

for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')

plt.xlabel("Company", size=14)
plt.ylabel("Closing Share Price", size=14)
plt.title("2018 Year End Stock Price")
plt.show()

# MM - Visual 3

plt.figure(figsize=(8, 8))

df4filt3 = df4[(df4.Date == '2017-06-30')]

plots = sns.lineplot(x="Company", y="Adj Close", data=df4filt3)

for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')

plt.xlabel("Company", size=14)
plt.ylabel("Closing Stock Price", size=14)
plt.title("2017 Mid Year Stock Price")
plt.show()

# MM - Other Insights

df['Adj Close'] = df['Adj Close'].round(2)
print("The maximum share price of Google between 2004 & 2020 is : $", end="")
dfmax = df['Adj Close'].max()
print(dfmax)

print("The maximum share price of Gamestop between 2002 & 2020 is : $", end="")
df1max = df1['Adj Close'].max().round(2)
print(df1max)

print("The maximum share price of Amazon between 1997 & 2020 is : $", end="")
df2max = df2['Adj Close'].max()
print(df2max)

df['Adj Close'] = df['Adj Close'].round(2)
print("The minimum share price of Google between 2004 & 2020 is : $", end="")
dfmin = df['Adj Close'].min()
print(dfmin)

print("The minimum share price of Gamestop between 2002 & 2020 is : $", end="")
df1min = df1['Adj Close'].min().round(2)
print(df1min)

df2['Adj Close'] = df2['Adj Close'].round(2)
print("The minimum share price of Amazon between 1997 & 2020 is : $", end="")
df2min = df2['Adj Close'].min()
print(df2min)

print("The average share price of Google between 2004 & 2020 is : $", end="")
dfav = df['Adj Close'].mean().round(2)
print(dfav)

print("The average share price of Gamestop between 2002 & 2020 is : $", end="")
df1av = df1['Adj Close'].mean().round(2)
print(df1av)

print("The average share price of Amazon between 1997 & 2020 is : $", end="")
df2av = df2['Adj Close'].mean().round(2)
print(df2av)

print("The increase in Google's Share Price from the lowest to highest point between 1997 & 2020 is: $", end="")
dfdiff = dfmax - dfmin
print(dfdiff)

print("The % increase in Google's Share Price from the lowest to highest point between 1997 & 2020 is: ", end="")
dfdiv = dfdiff / dfmin
dfper = dfdiv * 100
dfperd = dfper.round(0)
print(dfperd)

print("The increase in Gamestop's Share Price from the lowest to highest point between 1997 & 2020 is: $", end="")
df1diff = df1max - df1min
print(df1diff)

print("The % increase in Gamestop's Share Price from the lowest to highest point between 1997 & 2020 is: ", end="")
df1div = df1diff / df1min
df1per = df1div * 100
df1perd = df1per.round(0)
print(df1perd)

print("The increase in Amazon's Share Price from the lowest to highest point between 1997 & 2020 is: $", end="")
df2diff = df2max - df2min
print(df2diff)

print("The % increase in Amazon's Share Price from the lowest to highest point between 1997 & 2020 is: ", end="")
df2div = df2diff / df2min
df2per = df2div * 100
df2perd = df2per.round(0)
print(df2perd)

