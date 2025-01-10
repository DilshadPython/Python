name = input('Enter your name: ')
handle = open('words.txt', 'r')

counts = dict()

for line in handle:
    words = line.split()
    print('Read this line: ', words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        print('Counted: ', counts[word])

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('The bigest word is: ', bigword, ' and biggest count is: ', bigcount)
