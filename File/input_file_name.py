'''
You enter sample.txt file because we search for Hello word
'''
enter_file = input('Enter file name: ')

file_handle = open(enter_file)
count = 0

for line in file_handle:
	if line.startswith('Hello'):
		count = count + 1

print("There were ", count, 'hello words in ', enter_file)
