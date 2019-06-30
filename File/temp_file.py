import tempfile

def read_data(fil):
	fil.seek(0)
	data = fil.read()
	print(data)

fil = tempfile.TemporaryFile()
fil.write(b'Some temproraly data') # binary string

read_data(fil)