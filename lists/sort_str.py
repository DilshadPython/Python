"""
Demonstrates sorting lists of string items and notes tuple immutability.
"""

def demo_sort_strings():
    # Tuple immutability note: Tuples do NOT have a .sort() method because they are immutable.
    # To sort a tuple, use the built-in sorted(my_tuple) function which returns a new sorted list.

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
        'Southampton',  # Fixed typo: Southampton
        'Stoke City',
        'West Bromwich Albion',
    ]

    premier_league_teams.sort()
    print('Ascending order sort:', premier_league_teams[:5])

    premier_league_teams.sort(reverse=True)
    print('Descending order sort:', premier_league_teams[:5])

    return premier_league_teams

if __name__ == '__main__':
    demo_sort_strings()
