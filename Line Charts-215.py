## 2. Introduction To The Data ##

import pandas as pd

unrate = pd.read_csv('unrate.csv')
print(unrate)
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate.loc[0:11]

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt

plt.plot()
plt.show()

## 7. Adding Data ##

plt.plot(unrate['DATE'].head(12),unrate['VALUE'].head(12))

## 8. Fixing Axis Ticks ##

import matplotlib.pyplot as plt

plt.plot(first_twelve['DATE'],first_twelve['VALUE'])
plt.xticks( rotation=90 )
plt.show()

## 9. Adding Axis Labels And A Title ##

import matplotlib.pyplot as plt

plt.plot(first_twelve['DATE'],first_twelve['VALUE'])
plt.xticks( rotation=90 )
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()