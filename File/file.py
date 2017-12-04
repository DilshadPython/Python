

fileName = open('sample.txt', 'w')

fileName.write('Hello Python\n')

fileName.write('Hello Djnago\n')

fileName.write('Welcome to Flask Tutorials in Python\n')

fileName.close()



fread = open('sample.txt', 'r')

# we need to create a variable to stroe the data from text file
mytext = fread.read()

print(mytext)
fread.close()