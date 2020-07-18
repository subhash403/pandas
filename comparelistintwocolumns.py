'''
pandas comparing lists from two columns
'''

import pandas as pd

df = pd.read_csv('sheets\\emp10.csv')

rang = len(df.index)

df["Status"] = ""
print(df)
for i in range(0,rang):
    if sorted(df['list1'][i]) == sorted(df['list2'][i]):
        df.at[i, 'Status'] = 'Match'
    else:
        df.at[i, 'Status'] = 'MisMatch'

print(df)


