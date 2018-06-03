# Import all packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import datetime
import re
# Import all packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import datetime
import re

# Read in fakenames.csv file to DataFrame
file = '/Users/daviddolata/Desktop/Complaints.csv'
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
print(df_high['Company'].value_counts())
