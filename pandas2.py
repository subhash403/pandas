import pandas as pd
import numpy as np

# For Print the range of dates by using frequencies
a = pd.date_range('20200615', periods=10, freq='D')
print(a)

# np random
# For getting random data 10 columns and 4 rows
r = np.random.randn(10, 4)
print(r)

df = pd.DataFrame(r)
print(df)

# Use date_range as index

df = pd.DataFrame(r, index=a, columns=['A', 'B', 'C', 'D'])
print(df)

# For CHecking the colmns and shape
print(df.shape)
print(df.columns)
print(df.info())

# By default head or tail as 5
print(df.head(1))
print(df.tail())

# For Checking the Present Nul Values
print(df.isnull())

# For Count the null Values by Column
print(df.isnull().sum())

# For Drop the None/na Values by using dropna
print(df.dropna())

# For getting thespecific value from table
print(df.loc['2020-06-15','A'])
print(df.loc['2020-06-15',['A','B']])
print(df.iloc[0,0:2])
print(df.iloc[0:6,0:2])
#
print(df.iloc[0:7:2,0:3])

#

print(df.iloc[[0,1,5,6,8],:2])
# For Negative indexing
print(df.iloc[0:6,-3:-5:-1])
print("required values")
print(df.iloc[0:8:2,:-4:-2])
print(df.iloc[-1:-8:-2,-2:-5:-2])
# For Printing the Columns of the table
print(df.columns)

print(df.drop(columns=['A','D']))


# If you want to drop the Entire Column you can use df.dropna(axis=1) then it will delete the entire column
#df.value_counts()
print(df.corr())

#Describe gives calculations like  mean std min and percentages
print(df.describe())

# df.describe(include=['object'])
#df.describe(include=['all])

# Before comma is row and after comma is column
#df.iloc(row,col)
#df.loc(row,col)

# loc is for location and iloc is for indexed location
#df.loc[]