#How to open file to read and closed
import os
# getcwd Return a string representing the current working directory
print(os.getcwd())
pf = open('/home/dilmac/Devel/tutorials/Python/File/appendfile.txt', 'r')

myfile = pf.readlines()
print(myfile)
pf.close()
