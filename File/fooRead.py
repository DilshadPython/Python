# Open a file
fo = open("foo.txt", "r+")
string = fo.read(10)
print("Read String is : ", string)
# Close opend file
fo.close()
