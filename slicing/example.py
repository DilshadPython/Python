numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# slicing is [start:end:step]
print(numbers[1:8])
print(numbers[::10])
# start from 2, ended in 10, and each step is 2
print(numbers[2:10:2])
# start from 0 to the end and 3 steps
print(numbers[0::3])
print(numbers[::-1])
### start from index 3
print(numbers[4:])
###
print(numbers[-8:-2])

##
print(numbers[-3:2:-2])
