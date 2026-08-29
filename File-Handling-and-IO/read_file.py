# This is to scan the data in the file,
# and we don't need to write at the end clos() for this file we named to open when we use with:
with open('cities.txt', 'r') as f:
    lines = f.readlines()

# we have the data in the lines to read
for line in lines:
    # print('The, {} '.format(line)) # not look nice the layout
    print('The ', line.rstrip())

# This is tell you if the file is closed or not bt False or True
print(f.closed)