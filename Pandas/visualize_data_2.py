import pandas as pd
import datetime

import pandas_datareader
from pandas_datareader import data, wb

import matplotlib.pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')

start = datetime.datetime(2012, 1, 3)
end = datetime.datetime(2016, 12, 1)

output = data.DataReader('T', 'yahoo', start, end)

print(output.head())

print('\n##################NO HEAD ##############################')
print(output)

print('\nWe using graph from here')
output[['High', 'Low']].plot()

plt.legend()
plt.show()
