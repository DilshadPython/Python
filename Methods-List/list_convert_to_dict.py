import itertools

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

# create another list only int
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# zip both list together or pass them as iterators
addthem_tother = zip(nums, teams)

# pass them to dict function using list comprehentions instead of range
# use zip with slicing
premier_league = dict([(key, value) for key, value in zip(nums, teams)])

league = {i + 1: team for i, team in enumerate(teams)}

print(premier_league)
print('')
print(league)
