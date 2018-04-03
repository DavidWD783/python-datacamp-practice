# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/tips.csv'
# urlretrieve(url, 'tips.csv')
# file = 'tips.csv'

# # Use BeautifulSoup to print html of dataset
# from bs4 import BeautifulSoup
# import requests
# r = requests.get(url)
# text = r.text
# soup = BeautifulSoup(text, "lxml")
# print(soup.prettify())

# Create DataFrame
df = pd.read_csv(url, sep = ',', dtype=None, low_memory = False)
print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

# Create new sex_value column for Female/Male
# Import packages
import re

def create_column(sex_value):
	""" Takes input sex_value from sex column and creates new 0/1 column"""
	if sex_value == 'Male':
		return 1

	elif sex_value == 'Female':
		return 0

	else:
		return np.nan

df['new_sex_col'] = df['sex'].apply(create_column)
print(df.head())


