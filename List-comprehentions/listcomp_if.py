Num = range(1, 103)

# What it does loop throw and dispay all even number 
# if number mode by 2 == 0 than display even numbers
ListNum = [x for x in Num if x % 2 == 0]

print(ListNum)

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n')
sentence = 'Hello welcome to the party next week on '
sentence += 'Wednesday at 18:30 in London'

# we click this two sentence together using list comperhenseion
words = sentence.split(' ')

wordlen = [(word, len(word)) for word in words]
print(wordlen)

print('==============')
for x in wordlen:
	print(x)