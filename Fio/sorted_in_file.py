# read from the file and sorted before print in the screen
with open('cities.txt') as f:
    for line in sorted(f):
        print('Sorted in ', line.rstrip())
