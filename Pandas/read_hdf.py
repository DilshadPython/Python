import pandas as pd

'''
hdf  stand for High article data format HDF5
'''
data_frame = pd.read_csv('one_row.csv', names=['high', 'date'], index_col=0)

print(data_frame.head())

print('\n=====================')

# we create storage for hdf
store = pd.HDFStore('hdfstore2.h5')
print(store)

print('\n=====================')
store.put('d1', data_frame, format='table', data_colums=True)
print(store['d1'].shape)

store.close()

print('\n=====================')
hdf = pd.read_hdf('hdfstore2.h5', 'd1')

print(hdf)
