import itertools
import math

# create empty list
data = []

with open('math.txt') as mf:
    # use list comperhenstion
    data = [int(x) for x in mf.readlines()]
for size in range(2, 4):
    for current in itertools.combinations(data, size):
        if sum(current) == 2025:
            print(math.prod(current))
            break
