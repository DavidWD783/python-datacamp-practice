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

# Upload csv file and use header, delimiter, comment
df = pd.read_csv(url, header=3, delimiter = ' ', comment = '#')
print(df.head())
