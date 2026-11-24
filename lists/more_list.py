"""
Demonstrates list concatenation with += and mutating list elements by index.
"""

def demo_more_list_ops():
    # Fixed typo: Southampton
    team1 = ['Arsenal', 'Southampton', 'Man Utd']
    team2 = ['Liverpool', 'Man City', 'Chelsea', 'Tottenham']

    print('Team 1:', team1)
    print('Team 2:', team2)

    # In-place concatenation using +=
    team1 += team2
    print('\nCombined Team 1 after += Team 2:', team1)

    # Modify specific elements in place
    team1[0] = 'Man United'
    print('After team1[0] = "Man United":', team1)

    return team1

if __name__ == '__main__':
    demo_more_list_ops()
