# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/dob_job_application_filings_subset.csv'
urlretrieve(url, 'dob.csv')
file = 'dob.csv'

# # Use BeautifulSoup to print html of dataset
# from bs4 import BeautifulSoup
# import requests
# r = requests.get(url)
# text = r.text
# soup = BeautifulSoup(text, "lxml")
# print(soup.prettify())

# Create DataFrame
df = pd.read_csv(file, sep = ',', dtype=None, low_memory = False)
df_sub = df.loc[:,['Job #', 'Borough', 'House #', 'Initial Cost', 'Total Est. Fee']]
print(df_sub.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

# Create function to check Initial Cost and Total Est Fee for errors
# Then add new column to df_sub to show difference

# Import packages
import re

def cost_checker(row, pattern) :
	""" Checks columns for pattern, then finds difference """
	icost = row['Initial Cost']
	tef = row['Total Est. Fee']

	pattern1 = re.compile(pattern)
	if bool(pattern1.match(icost)) and bool(pattern1.match(tef)):
		icost = float(icost.replace('$', ''))
		tef = float(tef.replace('$', ''))

		return icost - tef

	else:
		return (NaN) 


df_sub['diff'] = df_sub.apply(cost_checker, axis = 1, pattern='\$\d*\.\d*')

print(df_sub.head())




