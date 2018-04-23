teams = [
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
print('All')
print(teams)
print('')

print('Delete the first 3 team from beginning')
del(teams[:3])

print(teams)
print('')

print('Delete from the end until the first 10 teams that is means: ')
print('The delete starting from index 10 down to 1 to see delete(West Ham United -)')
print('> Brighton & Hove Albion, ...... until Tottenham Hotspur')
del(teams[10::-1])
print(teams)
print('')

print('Delete the last 4 teams from the end')
del(teams[1::-1])
print(teams)
print('')