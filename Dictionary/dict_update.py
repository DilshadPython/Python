
account = {'fname': 'Dilshad', 'lname': 'Abdulla', 
			'address': '16 Glebe Road', 
			'date_of_birth': '28/03/1973', 'age': 41}

print(account)

print('\n Display keys ')
print(account.keys())

print('\n Display value: ')
print(account.values())

account.update({'fname': 'Azad', 'lname': 'Abdulla', 
				'address': '206 Valence Road', 
				'date_of_birth': '18/01/1975', 'age': 39})

print(account)

del account['date_of_birth']

print(account)
print()
print(len(account))

print('\n Display items:')
print(account.items())
