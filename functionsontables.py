'''
Functions on pandas tables
'''
import pandas as pd
import numpy as np
import os
r = np.random.randn(10, 4)
df = pd.DataFrame(r)

print(df)

# Function to apply to the whole table
def add(aaa, bbb):
    '''
    For adding the two numbers and apply function to pandas dataframe
    :param A: A is the First Value
    :param B: B is the Value
    :return: return the Value of addition
    '''
    return aaa+bbb

#For adding the 10 to all the values in the table
print(df.pipe(type))

print(df.apply(type))

print(df.pipe(add, 10))

print(df.pipe(np.mean))

print(df.apply(np.mean))


print(os.getcwd())

os.chdir('C:\\Users\\Venkat')

print(os.getcwd())

doc = pd.read_csv('C:\\Users\\Venkat\\PycharmProjects\\pandas\\sheets\\emp10.csv')
#doc = doc.rename(columns={'eid' : 'Employee_id'})
print(doc)
print(doc.shape)
print(doc.columns)
print(doc.dtypes)

doc2 = pd.read_csv('C:\\Users\\Venkat\\PycharmProjects\\pandas\\sheets\\emp10.csv', skiprows=1, names=['EMP_ID','NAME','DESIG','DOJ','SALARY'],header=0)

print(doc2)

doc3 = pd.read_csv('C:\\Users\\Venkat\\PycharmProjects\\pandas\\sheets\\emp10.csv', skiprows=[1,2,3],header=None,prefix='Subhash',verbose=True)

print(doc3)