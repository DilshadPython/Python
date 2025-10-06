import requests


main_url = 'https://pokeapi.co/api/v2/'


def get_connect_api(name):
	url = f'{main_url}/pokemon/{name}'
	response = requests.get(url)


	if response.status_code == 200:
		# print('Data found')
		data_poke = response.json()
		# print(data_poke)
		return data_poke
	else:
		print(f'Data not exist! {response.status_code}')

list_name = ['ditto', 'typhlosion', 'pikachu']

poke_name = list_name


poke_info = get_connect_api(poke_name[0]) 
poke_info_next = get_connect_api(poke_name[1]) 
poke_info_next_plus = get_connect_api(poke_name[2]) 


if poke_info:
	print(f'Name: {poke_info["name"].upper()}')
	print(f'ID: {poke_info["id"]}')
	print(f'Height: {poke_info["height"]}')
	print(f'Weight: {poke_info["weight"]}')

print()

if poke_info_next:
	print(f'Name: {poke_info_next["name"].upper()}')
	print(f'ID: {poke_info_next["id"]}')
	print(f'Height: {poke_info_next["height"]}')
	print(f'Weight: {poke_info_next["weight"]}')

print()
if poke_info_next_plus:
	print(f'Name: {poke_info_next_plus["name"].upper()}')
	print(f'ID: {poke_info_next_plus["id"]}')
	print(f'Height: {poke_info_next_plus["height"]}')
	print(f'Weight: {poke_info_next_plus["weight"]}')


print('\nAnother way:')
master_url = 'https://pokeapi.co/api/v2/'

def get_another_api(name):
	new_url = f'{master_url}/ability/{name}'
	response = requests.get(new_url)


	if response.status_code == 200:
		# print('Data found')
		data_poke = response.json()
		# print(data_poke)
		return data_poke
	else:
		print(f'Data not exist! {response.status_code}')


poke_name = 'battle-armor'

poke_new_info = get_another_api(poke_name) 

if poke_new_info:
	print(f'Name: {poke_new_info["name"].upper()}')
	print(f'ID: {poke_new_info["id"]}')
	print(f'is_main_series: {poke_new_info["is_main_series"]}')
	print(f'names: {poke_new_info["names"]}')