import json
import urllib
import requests


with open('stack.json', 'r') as json_data:
	data = json.load(json_data)
	print(data)
