'''
list comprehensions

[expr for val in collection]
[expr for val in collection if <test>]
[expr for val in collection if <test> and <test>]
'''
'''
GAUSS
len(p_remiders) = p+1/2
'''

premier_league = [
    'AFC Bournemouth',
    'Arsenal',
    'Brighton & Hove Albion',
    'Burnley',
    'Chelsea',
    'Crystal Palace',
    'Everton',
    'Huddersfield Town',
    'Leicester City',
    'Liverpool',
    'Manchester City',
    'Manchester United',
    'Newcastle United',
    'Southampton',
    'Stoke City',
    'Swansea City',
    'Tottenham Hotspur',
    'Watford',
    'West Bromwich Albion',
    'West Ham United'
]

football_team = []

test = [team for team in premier_league if team.startswith('M')]
print(test)

print()
start_with_s = [team for team in premier_league if team.startswith('S')]
print(start_with_s)
