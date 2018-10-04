import pandas as pd
import json

# we read the file from hdf not csv
data_frame = pd.read_hdf('hdfstore2.h5', 'd1')

# print(data_frame.head())
data_f = data_frame.reset_index()

data_f.to_json('convert_to_json.json')

data_frame_1 = pd.read_json('convert_to_json.json')

print(data_frame_1.head())


# If you want to download from url
import urllib.request

url_json = urllib.request.urlopen('http://json-schema.org/example/geo.json').read()

depth_data_frame = pd.read_json(url_json)

print(url_json)
