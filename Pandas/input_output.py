import pandas as pd

data_frame = pd.read_csv('WIKI-PRICES.csv')

print(data_frame.head())

# take the original file saved on different name as csv use to_csv() method
data_frame.to_csv('newfile.csv')
