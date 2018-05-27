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
# urlretrieve(url, 'dob.csv')
# file = 'dob.csv'

# Inspect file
df = pd.read_csv(url, sep=',', skiprows=12, delimiter=',', parse_dates=True, index_col='Date (MM/DD/YYYY)')
df.index.rename('Date', inplace=True)
print(df.head(2))
print(df.info())
print(df.columns)

# Setup plots for/from DataFrame
# temp = df['Temperature']
# graph = plt.plot(temp)
# plt.show()

# Plot DataFrame
# plot_list = df.iloc[:, 0:2]
# plot_list.plot(subplots=True)
# plt.show()
























