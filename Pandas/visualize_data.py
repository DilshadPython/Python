import pandas as pd
import datetime
import pandas.io.data as wb

import matplotlib.pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')

start = datetime.datetime(2012, 1, 3)
end = datetime.datetime(2016, 12, 1)

output = wb.DataReader('T', 'yahoo', start, end)

print(output.head())
