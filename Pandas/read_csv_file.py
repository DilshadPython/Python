import pandas as pd

# read csv file
df = pd.read_csv('data-store.csv')
df

# how to use the columns you need to display
df = pd.read_csv('data.csv', usecols=[1, 2, 3, 5])
df

# remove the 1 rows in the csv file
df = pd.read_csv('data.csv', header=1)
df


# change the header of the csv for None or removed
df = pd.read_csv('data.csv', header=None)
df

# change the herader names
df = pd.read_csv('data.csv', header=None, names=['year', 'level', 'coutries', 'companie', 'currency', 'values'])
df

# display only 3 rows
df = pd.read_csv('data.csv', nrows=3)
df

# create only columns you need 
df = pd.read_csv('data.csv', usecols=[3,4,5])
df

# change the columns named to NaN or nothing
df = pd.read_csv('data.csv', na_values=['Ford', 'Level 1'])
df

# how to create new csv file
df = pd.read_csv('data.csv')
# write to csv
df.to_csv('create_new_data.csv')
df


# skip the top rows which is 1 an display the names of rows header
df = pd.read_csv('data.csv', skiprows=1)
print(df.columns)

# write new csv file with name of the column listed
df = pd.read_csv('data.csv', skiprows=1)
# write to csv
df.to_csv('datas.csv', columns=['country', 'company', 'currency'])