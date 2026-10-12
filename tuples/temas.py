"""
Demonstrates sequence unpacking with football teams and heterogeneous types.
"""

def demo_team_unpacking():
    teams_tuple = ('Arsenal', 'Man United', 'Chelsea', 'Tottenham', 'Liverpool', 'Man City', 10)

    (a, b, c, d, e, f, g) = teams_tuple

    print('c and e:', c, e)
    print('All unpacked elements:', a, b, c, d, e, f, g)

    return c, e, g

if __name__ == '__main__':
    demo_team_unpacking()
