# Import all packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import datetime as dt
import re


# Read in Complaints.csv file to DataFrame
file = '/Users/daviddolata/Coding/Python/python-datacamp-practice/DataSets/Complaints.csv'
# col_list = ['Number', 'Gender', 'NameSet', 'GivenName', 'Surname', 'City', 'State', 'ZipCode', 'Country', 'EmailAddress', 'TelephoneNumber', 'Birthday']
df = pd.read_csv(file) 
date_obj = df['Date received'].astype(str)
date_time = pd.to_datetime(date_obj)
df.index = date_time
# print(df.head(2))

# Investigate companies
# print(df.Company.sort_values(ascending=True))
high_complaints = df['Company'].value_counts().rename('high_complaints')

df_high = df.merge(high_complaints.to_frame(), left_on='Company', right_index=True)
df_high = df_high.loc[df_high['high_complaints']>99, :]
# print(df_high.head(5))
# print(df_high['Company'].value_counts())

# Create student_loan DataFrame to inspect companies 
student_loan = df_high.loc[df_high['Sub-product']=='Federal student loan', :]
# print(student_loan.Company.value_counts())

# Create Navient DataFrame
navient = df_high.loc[df_high['Company']=='Navient Solutions, LLC.', :]
navient_sub = navient.loc[navient['Sub-product']=='I do not know', :]
# print(navient_sub['Sub-issue'].value_counts())

# Inspect ERC corporation
erc = df_high.loc[df_high['Company']=='ERC', :]
# print(erc.head(5))

# Inspect erc DataFrame
# erc['Sub-issue'].value_counts().plot()
# plt.show()
print(erc['Sub-product'].value_counts())


# No numeric data to plot
# navient_sub.plot()
# plt.show()
