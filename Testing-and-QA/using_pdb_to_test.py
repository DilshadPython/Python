import pdb

argsum = 0

def result(argsum, key):
    newval = argsum + key
    return newval

# to test use this line below after enter key, n, values, s 
pdb.set_trace()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

myresult = 0

for key in values:
    myresult = result(myresult, key)

print(myresult)
