#

with open('cities.txt', 'r') as f:
    name = f.readline()
    # you can add this in the print but in new version of python not need both are correct
    # in old version of python like python3.4 after end='' not read anymore
    print('\n\t: read one line', name, end='')
    print('\n\t: read one line', name)

    # this is read all contents horizontally as a list
    names = f.readlines()
    print('\n\t: read all lines', names)


