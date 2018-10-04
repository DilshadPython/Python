''' Here we use filter to remove empty string'''


capitales = [
	'Rom',
	'',
	'Paris',
	'Berlin',
	'',
	False,
	'',
	None,
	'London',
	'Stockholm',
	'Amstrdam',
	'',
	0.0,
	('Qairo'),
	'',
	{},
	'',
	'Erbil',
	0,
	'New Yourk',
	[],
	{0: 0}
]

''' the solutions for every empty string we use None as first argument of filter function '''

print('It removed all empty string replaced with None')
print(list(filter(None, capitales)))