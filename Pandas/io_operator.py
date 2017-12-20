import pandas as pd 

data_frame = pd.read_csv('WIKI-PRICES.csv')


# take the original file saved on different name as csv use to_csv() method
data_frame['date'].to_csv('one_row1.csv')
'''
The inplace flag causes the operation to happen in-place and return None,
instead of creating a new dataframe.
'''
data_frame.set_index('high', inplace = True)

data_frame['date'].to_csv('one_row1.csv')

data_frame = pd.read_csv('one_row1.csv')
print(data_frame.head())


print('\n=============================')
data_frame = pd.read_csv('one_row1.csv', index_col=0)
print(data_frame.head())

## add the header names to the csv file
print('\n=============================')
data_frame = pd.read_csv('one_row.csv', names=['date', 'high'], index_col=0)
data_frame.to_csv('onw_row2.csv')

# remove the date and hight in the csv file
data_frame.to_csv('onw_row4.csv', header=False)
print(data_frame.head())
