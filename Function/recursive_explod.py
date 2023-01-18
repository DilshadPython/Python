# Example of explod ==> explode('Python')-> 'P y t h o n'

def recursive_explode(word):
	if len(word) <=1 :
		return word
	else:
		return word[0] + ' ' + recursive_explode(word[1:])

print(recursive_explode(str(input('Enter any word: '))))