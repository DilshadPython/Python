import pandas as pd

sample = pd.Series([2, 7, 5, 10, 23, 6, 8], index = ['D', 'I', 'L', 's', 'h', 'a', 'd'])

# retrieve the first element

print(sample[0])

print('\n###########')

# retrieve up to forth elements
print(sample[:4])

print('\n###########')

# retrieve the last three elements
print(sample[-3:])

print('\n###########')

# retrieve the number of h in index list
print(sample['h'])

# retrieve the number of h in index list
print(sample[['h', 'D', 'L', 'a']])