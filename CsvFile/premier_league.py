
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

with open('premier.txt', 'w') as f:
	for team in teams:
		print(team, file=f)

