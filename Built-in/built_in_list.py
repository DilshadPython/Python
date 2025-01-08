
teams =  ['Arsenal', 'Southampton', 'Man Utd', 'Liverpool', 'Man City', 'Arsenal', 'Chelsea', 'Tottenham']

print(teams, '\n')
print('Display positions 4 and 1 in the list use teams[] >> ', teams[4], teams[1])
print('\n')

print('Display the number of obj in the list use len()')
print(len(teams))
print('\n')

print('Display from 2nd position to the end >> ', teams[2:], '\n')

print('Display from 3rd postion to 5th but do not display the 5th position itself: ', teams[3:5])
print('\n')

print('Use index() to enter the name of the team in the list to display the position:')
print(teams.index('Man Utd'), teams.index('Tottenham'), '\n')

print('Count how many obj in the list count() for example how many Arsenal team exist:')
print(teams.count('Arsenal'), ' << \n')

print('Copy the list to another list copy():')
# create an empty list
new_teams = []
print('The new empty list new_teams >> ', new_teams)
# copy the first team to the new teams
new_teams = teams.copy()
print('Display new_teams :', new_teams, ' << \n')

print('Change one to to another team use insert() it will take 2 arguments: ')
teams.insert(1, 'Leeds United')
print(teams)
print('\n')

print('Display the list before sorted() >> ', teams)
print('Sort the teams name alphabetically use sort() >> ', sorted(teams))
print('\n')

print('Display as reverse dont use reverse() function >> ', teams[-1:], ' << one way')
print(teams[-3:], '<< from current position tto the first')
print('\n')

print('Display as reverse dont use reverse() from right to 4th position >> ', teams[:-4])

print(teams[-3:], '<< from 3rd position to the first')
print('\n')

print('Remove one team from the list use pop() always take the last one >> ', teams.pop())
print(teams)
print('\n')

print('Adding new team to the teams list :')
print(teams.append('Newcastel United'))
print(teams)
print('\n')

print('Remove the name of the team in the teams list remove() always remove the first obj :')
print(teams.remove('Arsenal'))
print(teams)
print('\n')

print('Display the list form right to left reverse():\n ')
# reversed first with new list
teams.reverse()
print(teams, '\n')

print("Clear the list use clear() function or make it empty list >> ", teams.clear())
print('\n')