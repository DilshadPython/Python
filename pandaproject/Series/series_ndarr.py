import pandas as pd
import numpy as np

data = np.array(['d', 'i', 'l', 's', 'h', 'a', 'd'])

sample = pd.Series(data)


print(sample)

print('\n##################################\n')

new = pd.Series()
print(new)