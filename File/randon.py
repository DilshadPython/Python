import random
# this programm will rerandon every team name and ask you to input in the correct way as in the tuple
Teams = ('arsenal', 'southampton', 'manutd', 'liverpool', 'mancity', 'chelsea', 'tottenham', 'everton', 'atsonvilla', 'fullham')

team = random.choice(Teams)

correct = team

jumble = ' '

while team:
    position = random.randrange(len(team))
    jumble += team[position]
    team = team[:position] + team[(position + 1):]

print '\nThe jumble is ', jumble

enter = raw_input('Guess: ')
enter = enter.lower()

while (enter != correct) and (enter != ''):
    print '\nSorry that is not correct'
    enter = raw_input('Guess: ')
    enter = enter.lower()

if enter == correct:
    print 'Well done you win :)'

