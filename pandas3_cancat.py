'''
Pandas Cancatination
'''
import pandas as pd

a = pd.DataFrame({'Name':['subhash', 'ramesh', 'lokesh'], 'Age':[1, 2, 3]})

b = pd.DataFrame({'Name':['mahesh', 'subhash'], 'Age':[4, 5]}, index=[3, 4])

print("DataFrame A \n", a)

print("DataFrame B \n", b)

print("concatinate a and b dataframes")

ab = pd.concat([a, b])

print("Concat output\n", ab)

# For filtering the Specific Value
print(ab[ab['Name'] == 'subhash'])

# if we have dupliactes in the filters we can drop those duplicates

print(ab.drop_duplicates('Name'))

# Sort the values by age or Name
print(ab.sort_values('Name'))
print(ab.sort_values('Age'))

# Rename the column names using rename

print(ab.rename(columns={'Name':'Emp_Name', 'Age':'Emp_Age'}))

print(ab.describe())

print(ab.describe(include='object'))

print(ab.describe(include='all'))
