
							# w stand for written to the file
fileName = open('sample.txt', 'w')

fileName.write('Hello Python\n')

fileName.write('Hello Djnago\n')

fileName.write('Welcome to Flask Tutorials in Python\n')
# you need to closed otherwise not be saved what you write in the file
fileName.close()


						# r stand for reading to read what is in the file
fread = open('sample.txt', 'r')

# we need to create a variable to stroe the data from text file
mytext = fread.read()

print(mytext)
fread.close()