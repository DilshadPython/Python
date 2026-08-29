# Open a file
fo = open("foo.txt", "r+")
# read up to 100 characters
string = fo.read(47)
print("Read String is : ", string)

# to make sure what this file used for it will display r mean for read
print(fo.mode)

# read only the number of the content to read
print(fo.tell())

print(fo.fileno())

# Close opend file
fo.close()
