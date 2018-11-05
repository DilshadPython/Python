
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

with open('output.txt', 'w') as f:
    for team in teams:
        print(team, file=f)

with open('output.txt', 'a') as f:
    print('=' * 30, file=f)
    print('There are 20 teams in the file.', file=f)
