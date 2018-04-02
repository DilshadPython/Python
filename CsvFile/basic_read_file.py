
## This way is easy but maybe not safe
files = open('basic.txt')
text = files.read()
files.close()

print(text)

## the better way is like below:
print('###'*40)
with open('dilshad_bio.txt') as f:
	bio = f.read()
	# we don't need to close the file here

print(bio)