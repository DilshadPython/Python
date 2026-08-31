"""
Demonstrates filtering structured tuple sequences based on creation/founding year criteria.
"""

def demo_year_filtering():
    premier_league = [
        ('AFC Bournemouth', 1890),
        ('Arsenal', 1886),
        ('Brighton & Hove Albion', 1901),
        ('Burnley', 1882),
        ('Chelsea', 1905),
        ('Crystal Palace', 1905),
        ('Everton', 1878),
        ('Liverpool', 1892),
        ('Manchester City', 1880),
        ('Manchester United', 1878),
    ]

    # Teams founded before 1900
    older_teams = [team[0] for team in premier_league if team[1] < 1900]
    print('Teams founded before 1900:', older_teams)

    return older_teams

if __name__ == '__main__':
    demo_year_filtering()
