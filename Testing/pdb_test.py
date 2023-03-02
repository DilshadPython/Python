import pdb

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = 0

for key in values:
    result = result + key
    # this is stop you here to check the value of jey and result line by line
    # pdb.set_trace()

print(result)
