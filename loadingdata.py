'''
Loading data from csv,xlx, url
'''

import pandas as pd

df = pd.read_csv('http://winterolympicsmedals.com/medals.csv')

print(df.shape)

print(df.head())

df2 = pd.read_csv('http://winterolympicsmedals.com/medals.csv', nrows=5,usecols=[1,4,6])

print(df2)

df2.to_csv('sheets\\medalsedit.csv',index=False)