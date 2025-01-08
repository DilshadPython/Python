# with statment are use mostly for openen file which doesn't need
# to be clode() at the end where in other way to open need to be closed asap.
with open('withfiled.txt') as fh:
	for line in fh:
		line = line.rstrip()
		print(line)
print('Jobe done end of with!')

fh = open('withfiled.txt')
for line in fh:
	print(line)
fh.close()