# Every one in London not speak english
# answer will be = EoiLnse

def pick_first_letter(word):
	return word[0]

words = ['Every', 'one', 'in', 'London', 'not', 'speak', 'english']

to_do = list(map(pick_first_letter, words))
print(to_do)

another = ''
another = another.join(list(map(pick_first_letter, words)))
print(another)

print('===============================')

words = ['Every', 'one', 'in', 'London', 'not', 'speak', 'english']
def change_to_upper(word):
	to_upper = ''
	to_upper = to_upper.join(list(map(pick_first_letter, words))).upper()
	return to_upper

var = change_to_upper(words)
print(var)