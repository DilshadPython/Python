import numpy as np
import pandas as pd


labels = ['a', 'b', 'c', 'd', 'e']
_data = [5, 10, 15, 20, 25]
num_arr = np.array(_data)
dic = {'a': 5, 'b': 10, 'c': 15, 'd': 20, 'e': 25}

ser = pd.Series(data=labels)
print(ser)
