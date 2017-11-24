team1 =['Arsenal', 'Southampton' ,'Man Utd']
team2 = ['Liverpool', 'Man City', 'Chelsea' , 'Tottenham']
print('Team1: ', team1)
print('\n')
print('Team2: ', team2)

print('\n')
# How to cancatunaite to list and added them together
print('\tAdd the two teams together')
team1 += team2
print(team1)
print('\n')

# we change the 0 position to ManUnited in team1 and in team2 change position-2 to Arsenal
print('\tWe change the 0 position to ManUnited in team1 and in team2 change position-2 to Arsenal')
team1[0]='ManUnited'
team2[-2]='Arsenal'
print(team1)
print('\n')
print(team2)

print('\n')
del team2[1]
print('\tDelete first team in in team2: ')
print(team2)

print('\n')
print('\tAdd west Ham to the teams 2')
team2.append('Westham United')
print(team2)