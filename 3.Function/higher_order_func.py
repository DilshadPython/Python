# The higher order funcion example are map, filter and reduce

def sequre(num):
	return num * num


numbers = [1, 2, 3, 5, 7, 9, 4]
print('Numbers: ', numbers)

# What the map function does take the sequre function and applied to each numbers as sequnize
high_sq_num = list(map(sequre, numbers))
print('High order: ', high_sq_num)