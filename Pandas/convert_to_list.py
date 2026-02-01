import pandas as pd
from collections import OrderedDict, defaultdict
from indexing import data_frame

# print(data_frame.index)
print('\n Convert Data Frame to Dictionary: \n')
pd_dict = data_frame.to_dict('list')
print(pd_dict)
