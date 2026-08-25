# Example of explod ==> explode('Python')-> 'P y t h o n'

def remove_duplecate(word):
	print(word)
	if len(word) <=1 :
		return word
	elif word[0] == word[1]:
				# this is means go to next character and removed duplicated char
		return remove_duplecate(word[1:])
	else:
		return word[0] + remove_duplecate(word[1:])

print(remove_duplecate(str(input('Enter any word: '))))