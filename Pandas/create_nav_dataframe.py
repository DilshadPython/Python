import pandas as pd

automobils = {'Audi': ['A1', 'A2', 'A3', 'S3', 'A4', 'A5'],
              'BMW': ['F06', 'F20', 'F24', 'F30', 'F35', 'F40'],
              'MSD': ['MB-SLS', 'MB-CLA', 'MB-GLA', 'MB-SL', 'MB-R231', 'MB-G63'],
              'Ford': ['F150', 'Ranger', 'Transit', 'SuperDuty', 'Expedition', 'Edge'],
              'Nums': [44, 56, 72, 98, 2, 76],
              }

data_frame = pd.DataFrame(automobils)

print(data_frame)
print('\nData types')
print(data_frame.dtypes)

print('\nFords')
print(data_frame['Ford'])
print('\nAudi')
print('Audi ', data_frame['Audi'][3])

print('\nMercedes')
print(data_frame.MSD)
