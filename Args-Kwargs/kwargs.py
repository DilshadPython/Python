# (*args) is used to pass a non-keyworded, variable-length argument list,
# (**kwargs) is used to pass a keyworded, variable-length argument list.

def test_var_kwargs(word, **kwargs):
	print('Start test word', word)
	for key in kwargs:
		print('Inside for loop format is: {} {}'.format(key, kwargs[key]))

test_var_kwargs(word=8, myword='Hello', kwars=27)
