import pandas as pd
import urllib.request

from urllib.error import URLError, HTTPError


data_json = urllib.request.urlopen('https://btc-e.com/api/depth/btc_usd').read()
data_data_frame = pd.read_json(data_json)

print(data_json)

data_data_frame.to_pickle('pickle_file.pickle')