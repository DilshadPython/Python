# This is called event controll loop

average = 0.0
total = 0
count = 0

# the -1 here is the event which tell whileloop to stop
print('If you want to quit please enter grade (-1): ')
grade = int(input(' Enter a grade: '))
# while the year is less than 20 years
while grade != -1:
    # calculate the total with the grade entered
    total = total + grade
    count = count + 1
    # if we want to continue we will ask the user to enter another grade
    print('Enter another grade to continue or -1 to quit: ')
    grade = int(input(' Enter a grade: '))

average = total / count
print("Average grade :" + str(average))
