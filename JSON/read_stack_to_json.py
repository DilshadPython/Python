import json


with open('stack.json') as json_data:
	data = json.load(json_data)
	print(data)

print('##########################' + '##########################')
# python2 data.iteritems()
for key, value in data.items():
	print(key, value)

	