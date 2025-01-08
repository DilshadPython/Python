'''
Enter the file name is exisit in the current folder
'''
file_name = input('Enter file name: ')

'''
the if statment will ask you to enter directly without writing fname
this is only to reduce the time of writting fname or sname
'''
if len(file_name) < 1:
    file_name = 'sname.txt'

file_handle = open(file_name)

'''
we create a dictionary to add all word to this dictionary.
'''
w_dic = dict()

for line in file_handle:
    '''
    The rstrip() remove all white spaces between the words
    '''
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        ''' or '''
        # idiom: retrieve, create, update counter all in one line like below
        w_dic[word] = w_dic.get(word, 0) + 1
        # print(word, ' new ', w_dic[word])

# print(w_dic)
print('###' * 10)

''' create empty list '''
tmp = list()

for k,v in w_dic.items():
    print(k, v)
    ''' now we try flipped the key to the place of value '''
    new_tmp = (v, k)
    ''' we add the new tmp to the old one which is tmp '''
    tmp.append(new_tmp)

print(' Flipped: ', tmp)

''' we will sorted the tmp by value from minimum to maximum '''
tmp = sorted(tmp)
print(' Sorted: ', tmp)

''' if we want to sorted from maximum value to minimum value '''
tmp = sorted(tmp, reverse=True)
print(' Sorted:', tmp)
print(' Sorted:', tmp[:30])


for v, k in tmp[:35]:
    print(k, v)


file_handle.close()
