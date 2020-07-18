'''
compare twol columns and add match or mismatch in column
'''

import pandas as pd

df = pd.read_csv('sheets\\emp10.csv',header=0)

col = len(df.index)
df["MatchMisMatch"] = ""
for i in range(0,col):
     if df['Name1'][i] == df['Name2'][i]:
         df.at[i,'MatchMisMatch'] = 'Match'
     else:
         df.at[i, 'MatchMisMatch'] = 'MisMatch'


df2 = df[['Name1','Name2','MatchMisMatch']]

df2.to_csv('sheets\\empcompare.csv')