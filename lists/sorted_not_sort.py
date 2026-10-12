"""
Demonstrates sorted() function usage without mutating the original list.
"""

def demo_sorted_vs_sort():
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
        'Southampton',  # Fixed typo: Southampton
        'Stoke City',
        'West Bromwich Albion',
    ]

    # sorted() creates a new list
    sorted_teams = sorted(premier_league)
    print('New sorted list (first 3):', sorted_teams[:3])
    print('Original list unchanged (first 3):', premier_league[:3])

    return sorted_teams

if __name__ == '__main__':
    demo_sorted_vs_sort()
