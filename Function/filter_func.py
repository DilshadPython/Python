# filter is another high order function
# Filter will take the function and apply to all the sequnize has given and return
# only those are match to even 
# % this is moduler means the reminder

def even_func(num):
	if num % 2 == 0:
		return True
	else:
		return False

numbers = list(range(1, 12))
print(numbers)
# filter will apply the function to the number if the reminder is 0 tahn return evens 
# numbers only
evens = list(filter(even_func, numbers))
print(evens)