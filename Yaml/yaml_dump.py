import yaml

data_list = [1, 3, 5, 7, 'hi']
data_tuple = ('a', 'b', 'c', 'de')
data_dict = {
	'a': 22,
	'b': 7,
	'c': 87,
	'd': 'Python',
}

load_to_yaml = yaml.dump(data_list, default_flow_style=False)
load_to_yaml1 = yaml.dump(data_tuple, default_flow_style=False)
load_to_yaml2 = yaml.dump(data_dict, default_flow_style=False)

print(load_to_yaml)
print(load_to_yaml1)
print(load_to_yaml2)