x = 'cat'

def func():
	x = 'Bird'
	
	def sub_func():
		x = 'Dog'
		y = 'Elephan'
		print(x)
	sub_func()
func()

cat, dog, Bird, Elephan