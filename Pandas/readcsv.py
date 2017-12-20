import pandas as pd 

data_frame = pd.read_csv('newfile.csv')

print(data_frame.head())

data_frame['adj_open'].to_csv('onerow.csv')

one_row = data_frame.set_index('volume')

print('\n+++++++++++++++++++++++++++++==========++++++++++++++++++++++++++')
print('\n+++++++++++++++++++++++++++++==========++++++++++++++++++++++++++')
print(one_row.head())

data_frame = data_frame.set_index('volume', inplace = True)
print('#####################################################################')
print(data_frame.head())

data_frame['adj_open'].to_csv('onerow1.csv')