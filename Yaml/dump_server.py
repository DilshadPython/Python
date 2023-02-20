import yaml
import json

with open('app.yaml') as fhandler:
	data_structure = yaml.full_load(fhandler)
	print('Yaml load\n')
	print(data_structure)

print('JSON dump\n')
print(json.dumps(data_structure, indent=4, separators=(',', ': ')))
