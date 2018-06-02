# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 
import datetime
import re

# Create dict d
# d = {'a': [1], 'b': [2]}
# print(d)

# # Convert dict 'data' into DataFrame
# df = pd.DataFrame(data=d)
# print(df)

# Create DataFrame using zip of lists
# names = ['One', 'Two', 'Three', 'Four']

# dates = [0, 1, 2, 3]

# ages = [20, 30, 40, 50]

# places = ['City', 'Country', 'Suburb', 'Desert']

# list_labels = ['Name', 'Date', 'Age', 'Location']

# list_cols = [names, dates, ages, places]

# zipped = list(zip(list_labels, list_cols))
# # print(zipped)

# data = dict(zipped)

# df = pd.DataFrame(data)
# print(df.columns)
# print(df.index)
# print(df)

# # Create DataFrame from list using key/value pairs
# cities = ['Manheim', 'Preston park', 'Biglerville', 'Indiana', 'Curwensville', 'Crown', 'Harveys lake', 'Mineral springs', 'Cassville', 'Hannastown', 'Saltsburg', 'Tunkhannock', 'Pittsburgh', 'Lemasters', 'Great bend']

# state = 'PA'

# data = {'state': state, 'city': cities}

# df = pd.DataFrame(data)
# print(df.head())

# Import dataset from url
from urllib.request import urlretrieve
# url = 'https://assets.datacamp.com/production/course_1639/datasets/weather_data_austin_2010.csv'
url = 'https://assets.datacamp.com/production/course_1639/datasets/austin_airport_departure_data_2015_july.csv'
# url = 'https://assets.datacamp.com/production/course_1639/datasets/NOAA_QCLCD_2011_hourly_13904.txt'
# urlretrieve(url, 'dob.csv')
# file = 'dob.csv'

# Inspect file
# df = pd.read_csv(url, sep=',', delimiter=',')
df = pd.read_csv(url, sep=',', skiprows=12, delimiter=',')
# df.index.rename('Date', inplace=True)
date_time = df['Date (MM/DD/YYYY)']
# print(date_time)
date_time = pd.to_datetime(date_time)
df.index = date_time.rename('Date') 
print(df.head(2))
print(df.info())
# print(df.columns)

# df_temp = df.resample('D').mean()
# print(df_temp.head(2))
# df1 = df_temp.loc['2010-01-01':'2010-01-08'].plot(style='b.-', subplots=True)
# plt.show()

# # Inspect 'Scheduled Elapsed Time(Minutes)'
# print(df['Scheduled Elapsed Time(Minutes)'][0:5])
# df.plot(kind='hist', y='Scheduled Elapsed Time(Minutes)', bins=20)
# plt.show()


# Setup plots for/from DataFrame
# temp = df['Temperature']
# graph = plt.plot(temp)
# plt.show()

# Plot DataFrame
# plot_list = df.iloc[:, 0:2]
# plot_list.plot(subplots=True)
# plt.show()
























