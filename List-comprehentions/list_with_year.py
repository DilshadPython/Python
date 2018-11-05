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
    ('AFC Bournemouth', 1980),
    ('Arsenal', 1944),
    ('Brighton & Hove Albion', 1985),
    ('Burnley', 1983),
    ('Chelsea', 1990),
    ('Crystal Palace', 1991),
    ('Everton', 1960),
    ('Huddersfield Town', 1995),
    ('Leicester City', 1989),
    ('Liverpool', 1941),
    ('Manchester City', 1991),
    ('Manchester United', 1940),
    ('Newcastle United', 1988),
    ('Southampton', 1985),
    ('Stoke City', 1986),
    ('Swansea City', 1987),
    ('Tottenham Hotspur', 1977),
    ('Watford', 1995),
    ('West Bromwich Albion', 1970),
    ('West Ham United', 1978)
]

football_team = []

print('Team before 1990')
team_before_1990 = [team for (team, year) in premier_league if year < 1990]
print(team_before_1990)

print(0)
print('Team after 1989')
team_after_1989 = [team for (team, year) in premier_league if year > 1989]
print(team_after_1989)
