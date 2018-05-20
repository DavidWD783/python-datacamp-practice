# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_1639/datasets/messy_stock_data.tsv'
# urlretrieve(url, 'dob.csv')
# file = 'dob.csv'

# Create DataFrame
# Create DataFrame
df = pd.read_csv(url, sep = ',', skiprows = 3, header=0, dtype=None, low_memory = False)
df = df.drop(0)
df = df.drop(3)
df = df.drop(6)
df = df.reset_index(drop=True)
print(df)

# print(df.tail())
# print(df.info())
# print(df.describe())