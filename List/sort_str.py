'''
You can not use sort with tuple because tuple is immutable object you can't chang it. 
'''
print('You can not use sort with tuple because tuple is immutable object you can\'t chang it.')
print()
print()
premier_league_teams = [
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

premier_league_teams.sort()
print(premier_league_teams)

print('###' * 30)
print()

premier_league_teams.sort(reverse=True)
print(premier_league_teams)
