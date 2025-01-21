# rstrip() remove extra line show the reading more nice
with open('cities.txt', 'r') as f:
    for line in f:
        # using rstrip()
        print('Hi,', line.rstrip())