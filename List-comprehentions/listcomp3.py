file = open('grades.txt')

# rstrip() remove \n
numbercom = [x.rstrip() for x in open('numbers.txt')]

print(numbercom)
