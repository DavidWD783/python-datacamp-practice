# Import all packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import datetime as dt
import re


# Read in sales.csv file to DataFrame
file = '/Users/daviddolata/Coding/Python/python-datacamp-practice/sales/sales.csv'
# col_list = ['Number', 'Gender', 'NameSet', 'GivenName', 'Surname', 'City', 'State', 'ZipCode', 'Country', 'EmailAddress', 'TelephoneNumber', 'Birthday']
df = pd.read_csv(file, index_col='month')
# print(df.head())

# Access specific cols/rows/values
# print(df.iloc[2, [0,1]])
# print(df[(df['eggs']>100) & (df['salt']<100)])
print(df.loc[:, df.notnull().all()])