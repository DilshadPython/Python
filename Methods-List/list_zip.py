numbers = [2, 5, 11, 9, 0, 7, 15]

num_str = ['two', 'five', 'eleven', 'nine', 'zero', 'seven', 'fiftting']

# No iterables are passed 
put_together = zip()

# converting itertor to list
main_list = list(put_together)
print(main_list) # empty list

# now we will pass two iterables
put_together = zip(numbers, num_str)

# convert iterator to the dictionary
mydict = dict(put_together)
print(mydict)
