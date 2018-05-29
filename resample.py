# Import all packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import datetime
import re

# Import dataset from url
from urllib.request import urlretrieve
# url = 'https://assets.datacamp.com/production/course_1639/datasets/weather_data_austin_2010.csv'
url = 'https://assets.datacamp.com/production/course_1639/datasets/austin_airport_departure_data_2015_july.csv'
# urlretrieve(url, '')
# file = ''

# Inspect file
df = pd.read_csv(url, sep=',', skiprows=12, delimiter=',', parse_dates=True, index_col='Date (MM/DD/YYYY)')
df.index.rename('Date', inplace=True)
print(df.head(2))
print(df.info())
# print(df.describe())

# Resample 
res = df.resample('D').mean()
print(res.head())
print(res.info())
# list1 = [res.min(), res.max()]
# print(list1)