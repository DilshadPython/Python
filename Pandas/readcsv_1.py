import pandas as pd


data_frame = pd.read_csv('WIKI-PRICES.csv')

print(data_frame.head())

data_frame['close'].to_csv('one_row.csv')

one_row = data_frame.set_index('date')

print('\n+++++++++++++++++++++++++++++==========++++++++++++++++++++++++++')
print('\n+++++++++++++++++++++++++++++==========++++++++++++++++++++++++++')
print(one_row.head())

two_row = data_frame.set_index('date', inplace = True)
print('#####################################################################')
print(two_row)

two_row['volume'].to_csv('onerow_1.csv')