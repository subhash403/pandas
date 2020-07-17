'''
pandas visualization
'''
import pandas as pd

cars = pd.read_csv('sheets\\usedcars.csv')

print(cars.shape)

print(cars['price'].plot())
