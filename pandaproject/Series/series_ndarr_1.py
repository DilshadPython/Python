import pandas as pd
import numpy as np

data = np.array(['D', 'I', 'L', 'S', 'H', 'A', 'D'])

sample = pd.Series(data, index=[100, 101, 102, 103, 104, 105, 106])


print(sample)