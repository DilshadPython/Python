'''
You enter sample.txt file because we search for Hello word then run try
But if you enter the wrong file name then except line will run.
'''
enter_file = input('Enter file name: ')

try:
	file_handle = open(enter_file)
except:
	print('The file can not be open and not exist.', enter_file)
	'''
	we have to add quit function otherwise for loop will continue and display Traceback
	That means stopped Traceback
	'''
	quit()

count = 0

for line in file_handle:
	if line.startswith('Hello'):
		count = count + 1

print("There were ", count, 'hello words in ', enter_file)
