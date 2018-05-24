# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_1639/datasets/auto-mpg.csv'
# urlretrieve(url, 'auto-mpg.csv')
# file = 'auto-mpg.csv'

# Upload csv file and use header, delimiter, comment
df = pd.read_csv(url,  sep = ',')
print(df.head())
# print(df.info())
# print(df.shape)
# print(df.describe())

# Your job is to compute the minimum and maximum values 
# of the 'mpg' and 'accel' columns and generate a line plot 
# of the mean value of each column/field. 
# To perform this step, you'll use the .mean() method with
# the keyword argument axis='columns'. This computes the 
# mean across all columns per row.

# Find min and max values of columns
mins = df[['mpg', 'accel']].min()
print(mins)

maxs = df[['mpg', 'accel']].max()
print(maxs)

diff = maxs - mins
print(diff)

# Find the mean value of all columns and plot
df.mpg.plot(kind='hist')
plt.show()