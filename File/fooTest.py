# Open a file
fo = open("foo.txt", "r+")
string = fo.read(10)
print("Read String is : ", string)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
string = fo.read(10)
print("Again read String is : ", string)
# Close opend file
fo.close()
