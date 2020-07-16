"""
Pandas Document
"""
import pandas as pd
import numpy as np

print(np.__version__)

a = ([10, 20, 30])

# First Series Object

a = pd.Series([10, 20, 30])
print(a)
print(type(a))

# Series with Renaming the indexes

a = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(a)
print(type(a))

#Sereies wit None value

a = pd.Series([10, 20, np.nan])
print(a)
print(type(a))

# Single Dimension DataFrame

a = pd.DataFrame([10, 20, np.nan])
print(a)
print(type(a))

#First Dataframe with multi dimensions

a = [["Subhash", 97], ["mahesh", 99], ["ramesh", 100]]
print(a)
df = pd.DataFrame(a)
print(df)

# For Renaming the Comuns with what ever we need

b = [["Subhash", 97], ["mahesh", 99], ["ramesh", 100]]
df = pd.DataFrame(b, columns=['Name', 'Marks'])
print(df)

# For Printing the specific Column

c = [["Subhash", 97], ["mahesh", 99], ["ramesh", 100]]
df = pd.DataFrame(c, columns=['Name', 'Marks'])
print(df['Name'])

# From Dictionaries
a = {'Name':['ramesh', 'subhash'], 'Age':[12, 13]}
df = pd.DataFrame(a, index=[3, 4])
print(df)

# numpy array to DataFrame
a = np.array([[1, 2], [3, 4]])
print(a)

#array to DataFrame
df = pd.DataFrame(a)
print(df)

#DataFrame to array
a = np.array(df)
print(a)
