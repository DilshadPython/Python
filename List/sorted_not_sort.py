
# print(help(sorted))
'''
Help on built-in function sorted in module builtins:

sorted(iterable, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.
(END)
'''

premier_league = [
	'Manchester City',
	'Manchester United',
	'Liverpool',
	'Tottenham Hotspur',
	'Chelsea',
	'Arsenal',
	'Burnley',
	'Leicester City',
	'Everton',
	'AFC Bournemouth',
	'Watford',
	'Newcastle United',
	'Brighton & Hove Albion',
	'West Ham United',
	'Swansea City',
	'Huddersfield Town',
	'Crystal Palace',
	'Southhanpton',
	'Stoke City',
	'West Bromwich Albion',	
]
teams = sorted(premier_league)

print(teams)