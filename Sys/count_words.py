import sys

'''
This count_words.py file read any files ended with 
(.txt or .dat or .md ) and count each words has been
writing and display all duplications or more than two
times repeated.
# To run python count_words.py text.dat or file.txt
'''

def count_words(filename):
	results = dict()

	with open(filename, 'r') as f:
		for line in f:
			for word in line.split():
				results[word] = results.setdefault(word, 0) + 1

	for word, count in sorted(results.items(), key=lambda x: x[1]):
		print('{} {}'.format(count, word))

count_words(sys.argv[1])

