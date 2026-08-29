# we created the file grade.txt created before
# create bar to empty string can be anything
# first for loop read the file grade.txt
# second for loop start from 1 until reach the end of the number in each line and added + 1
# the if statment say each number % 5 remineded to 0
# set the bar to # and increment by 1
# the results shows howmany times the number % 5 == 0 for each number are show #

bar = ''

for grade in open('grade.txt'):
    for i in range(1, int(grade) + 1):
        if i % 5 == 0:
            bar = bar + '#'
    print(bar, i)
    bar = ''
