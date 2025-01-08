### map function will take 2 arguments:
#### map(function, (list or tuple or itrable))

#### The map function will take 2 argument first is a function second is a list or tuple or other itrable object

#### Explain:
		Data: x1, x2, x3, ..., xnum
		Function: f()

		mpp(f, data):
			Returns iterator over each data
			f(x1), f(x2), f(x3), ..., f(xnum)

#### Calculate tempratures: f = 9/5.c + 32

#### The filter function will take 2 argument first is a function second is a list or tuple or other 	itrable object

#### False values in python """ 0, '', 0.0, [], (), {}, False, None """

### In python 3+, reduce is not builtin function, moved to functools module it need to be like 			from functools import reduce 

#### The reduce function will take 2 argument first is a function second is a list or tuple or other 	itrable object

#### Explain:
	Data: [x1, x2, x3, ..., xn]
		Function: f(i, j)

	reduce(f, data):
		step 1: val1 =f(x1, x2)
		step 1: val2 =f(val1, x3)
		step 1: val3 =f(val2, x4)
		.
		.
		step n-1: valn-1 = f(valn-2, xn)

		More:
		    Returns f(f(f(x1, x2), x3), x4), ..., xn)
