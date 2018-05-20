# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Create dict d
# d = {'a': [1], 'b': [2]}
# print(d)

# # Convert dict 'data' into DataFrame
# df = pd.DataFrame(data=d)
# print(df)

# Create DataFrame using zip of lists
names = ['One', 'Two', 'Three', 'Four']

dates = [0, 1, 2, 3]

ages = [20, 30, 40, 50]

places = ['City', 'Country', 'Suburb', 'Desert']

list_labels = ['Name', 'Date', 'Age', 'Location']

list_cols = [names, dates, ages, places]

zipped = list(zip(list_labels, list_cols))
# print(zipped)

data = dict(zipped)

df = pd.DataFrame(data)
print(df)