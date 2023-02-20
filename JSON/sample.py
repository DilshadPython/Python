# JSON Java Script Object Notation

import json
import io
# print(dir(json))
# OUTPUT
'''
['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', 
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', 
'__spec__', '__version__', '_default_decoder', '_default_encoder', 'decoder', 'dump', 'dumps', 
'encoder', 'load', 'loads', 'scanner']
'''
# INFO
# we add this encoding='utf-8' if there a character not available in
# english alphabet

with open('my_data.txt') as jsonfile:
    # try:
    load_data = json.load(jsonfile)
    print(load_data, 'Loading')
    output_data = json.dump(load_data)
    print(output_data)
    # except ValueError: #json.decoder.JSONDecoder:

    # 	print('Decoding JSON has faild')


# with io.open(path, 'data_1.txt', 'r') as jsonfile:
# 	print(path)
# 	load_data = json.load(jsonfile)
# 	print(load_data)
# 	output_data = json.dump(load_data)
# 	print(output_data)
