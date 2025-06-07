
''' w stand for written to the file '''
FILENAME = open('sample.txt', 'w')
filename = open('samle_1.txt', 'w')

FILENAME.write('Hello Python\n')

FILENAME.write('Hello Djnago\n')

FILENAME.write('Welcome to Flask Tutorials in Python\n')

filename.write('Welcome to new Tutorials in ReactJs\n' * 10)

'''
	you need to closed otherwise not be saved what you write in the file.
'''

FILENAME.close()
filename.close()

'''
	r stand for reading to read what is in the file 
	we need to create a variable to stroe the data from text file
'''
# r stand for reading to read what is in the file
FREAD = open('sample.txt', 'r')

MY_TEXT = FREAD.read()
print(MY_TEXT)
FREAD.close()
