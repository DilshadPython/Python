import json


with open('data_1.txt') as me:
	data = json.load(me)

	for x in data:
		print(x[''], '-', x[''])