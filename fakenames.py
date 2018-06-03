# Import all packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import datetime
import re

# Read in fakenames.csv file to DataFrame
file = '/Users/daviddolata/Desktop/FakeNames.csv'
col_list = ['Number', 'Gender', 'NameSet',
            'GivenName', 'Surname', 'City', 'State', 'ZipCode', 'Country', 'EmailAddress', 'TelephoneNumber', 'Birthday']
df = pd.read_csv(file, index_col='Number', sep=',', delimiter=',', nrows=50, usecols=col_list)
print(df.head(2))
