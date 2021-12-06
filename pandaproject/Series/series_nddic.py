import pandas as pd
import numpy as np

data = {'D' : 0., 'I' : 1., 'L': 2., 'S': 3., 'H': 4., 'A': 5., 'D': 6.}

sample = pd.Series(data, index=['D', 'I', 'L', 's', 'h', 'A', 'd'])


print(sample)