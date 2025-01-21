# This is to scan the data in the file
with open('cities.txt', 'r') as f:
    lines = f.readlines()

# we have the data in the lines to read
for line in lines:
    # print('The, {} '.format(line)) # not look nice the layout
    print('The ', line.rstrip())