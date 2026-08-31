"""
Demonstrates list sorting, filtering, and manipulation on football team datasets.
"""

def manage_football_teams():
    teams = ['Liverpool', 'Manchester City', 'Chelsea', 'Arsenal', 'Tottenham']
    print('Original teams:', teams)

    # Sort in-place alphabetically
    teams.sort()
    print('Sorted teams:', teams)

    # Reverse sort order
    teams.sort(reverse=True)
    print('Reverse sorted teams:', teams)

    # Custom key sort: by length of team name
    teams.sort(key=len)
    print('Sorted by length of team name:', teams)

    return teams

if __name__ == '__main__':
    manage_football_teams()
