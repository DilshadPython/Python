sentence = 'To better understand how functions work, line lets create one. To type this program\
             into line work the file editor and save it as hello on mu function and so on'

sentence += ' The first line is a def To statement line'

words = sentence.split(' ')
words = sorted(words)
print('Sentence is sorted order: \n')
print(words)

numwords = {}

for i in range(0, len(words)):
    if words[i] in numwords:
        numwords[words[i]] += 1
    else:
        numwords[words[i]] = 1

print('###' * 30)
print('Word list and count: \n')
for key in numwords.keys():
    print(key, '\t\t', numwords[key])
