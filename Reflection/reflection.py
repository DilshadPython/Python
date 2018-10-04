def reflect(seq):
	ftype = type(seq)
	emptyseq = ftype()

	if seq == emptyseq:
		return emptyseq

	restrev = reflect(seq[1:])
	first = seq[0:1]

	result = restrev + first
	return result

print(reflect([2, 4, 5, 6, 8, 9]))
print(reflect('Hello world'))