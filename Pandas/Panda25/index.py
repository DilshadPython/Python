
import pandas as pd

automobils = {
    'Nums': [44, 56, 72, 98, 2, 76, 99, 76],
    'Car1': ['A1', 'A2', 'A3', 'S3', 'A4', 'A5', 'A6', 'A7'],
    'Car2': ['BMW-06', 'BMW-20', 'BMW-24', 'BMW-30', 'BMW-35', 'BMW-40', 'BMW-45', 'BMW-50'],
    'Car3': ['MB-SLS', 'MB-CLA', 'MB-GLA', 'MB-SL', 'MB-R231', 'MB-G63', 'ML250', 'ML'],
    'Names': ['Alan', 'Tom', 'Chris', 'Ema', 'Dave', 'Sam', 'Loren', 'Kaio'],
    'Car4': ['F150', 'Ranger', 'Transit', 'SuperDuty', 'Expedition', 'Edge', 'FT', 'FTT'],
}
print('\n')

print('\n=========================Data Frames=============================\n')
data_frame = pd.DataFrame(automobils)
print(data_frame, 'Hello')

# In the printif you looked at the dic in the output sorted first Car1-4
# than name and nums
# print(data_frame)

# print out (0-7) dtypes=int64
print('\n========================= Index =============================\n')
print(data_frame.index)

# data_frame as index bring the Names to the front, return the value
print('\n====================== Set_index ============================\n')
result = data_frame.set_index('Names')
print(result)

# data_frame as index bring the Car3 to the front, return the value
print('\n====================== set_index ============================\n')
result = data_frame.set_index('Car3')
print(result)

print('\n====================== index ================================\n')
print(data_frame.index)

print('\n======================= Head ================================\n')
print(data_frame.head())

