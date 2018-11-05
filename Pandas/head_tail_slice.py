import pandas as pd

automobils = {'Audi': ['A1', 'A2', 'A3', 'S3', 'A4', 'A5', 'A6', 'A7'],
              'BMW': ['BMW-06', 'BMW-20', 'BMW-24', 'BMW-30', 'BMW-35', 'BMW-40', 'BMW-45', 'BMW-50'],
              'MSD': ['MB-SLS', 'MB-CLA', 'MB-GLA', 'MB-SL', 'MB-R231', 'MB-G63', 'ML250', 'ML'],
              'Ford': ['F150', 'Ranger', 'Transit', 'SuperDuty', 'Expedition', 'Edge', 'FT', 'FTT'],
              'Nums': [44, 56, 72, 98, 2, 76, 99, 76],
              }

data_frame = pd.DataFrame(automobils)

# When you call the head() only display the first 5 column
print(data_frame.head())

# display all columns
print('\n-----------------------------------------')
print(data_frame)

# cut the last 5 column
print('\n-----------------------------------------')
print(data_frame.tail())

# display the first three column
print('\n-----------------------------------------')
print(data_frame.head(3))

# display the last two column
print('\n-----------------------------------------')
print(data_frame.tail(3))

# slicing
# display the first two column
print('\n-----------------------------------------')
print(data_frame['MSD'][4])

print('\n-----------------------------------------')
print(data_frame['Audi'][3])

print('\n-----------------------------------------')
print(data_frame['Nums'][5])
