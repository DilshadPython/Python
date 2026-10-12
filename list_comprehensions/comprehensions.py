"""
Demonstrates filtering string lists using string method predicates in comprehensions.
"""

def demo_string_comprehensions():
    premier_league = [
        'AFC Bournemouth', 'Arsenal', 'Brighton & Hove Albion', 'Burnley',
        'Chelsea', 'Crystal Palace', 'Everton', 'Huddersfield Town',
        'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United',
        'Newcastle United', 'Southampton', 'Stoke City', 'Swansea City',
        'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United'
    ]

    # Filter teams starting with 'M'
    m_teams = [team for team in premier_league if team.startswith('M')]
    print('Teams starting with M:', m_teams)

    # Filter teams starting with 'S'
    s_teams = [team for team in premier_league if team.startswith('S')]
    print('Teams starting with S:', s_teams)

    return m_teams, s_teams

if __name__ == '__main__':
    demo_string_comprehensions()
