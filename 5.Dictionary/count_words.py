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
    # print('== Before ==\n')
    line = line.rstrip()
    # print(line)

    '''
	The split() add all word to '' 
	'''
    # print("-- adding '' --\n")
    words = line.split()
    # print(words)
    for word in words:
        '''
        	This is very important to understand
        	the get(word, -99) is display the word which is exisit and -99 is a default value
        	that the word not exisit
        '''
        # print('==>', word, w_dic.get(word, -99))

        '''
        	The .get(word, 0) if the word is there than give me back if not than display as 0
        '''
        # privous_count = w_dic.get(word, 0)
        # print(' The number of the word(', word, ') was: ', privous_count)

        # new_count = privous_count + 1
        # w_dic[word] = new_count
        # print('After we found another one or new (', word, ') become: ', new_count)

        ''' or '''
        # idiom: retrieve, create, update counter all in one line like below
        w_dic[word] = w_dic.get(word, 0) + 1
        # print(word, ' new ', w_dic[word])

        '''
        After we add the above code from privous_count to new_count we do not need the below codes.
        '''

        # if word in w_dic:
        #     ''' if the word is there added 1 to it or incremented'''
        #     w_dic[word] = w_dic[word] + 1
        #     # print(' ** The word exists ** ')
        # else:
        #     ''' if the word is new then display as new word or if is new insert to as one'''
        #     w_dic[word] = 1
            # print(' == New word == \n')
        # print(word, w_dic[word])

# print('\n ===== Total words in the dictionary with the value ==== \n')
# print(' =======================================================')

''' This print display all with how many time the word has been repeated '''
print(w_dic)

'''
dict{'key': 'value'}
Now we try which word are most repeated?
k = key
v = value
'''

max_word = -1
find_word = None
for k, v in w_dic.items():
	print(k, ':', v)
	if v > max_word:
		max_word = v
		find_word = k

print('===================================')
print('The End. ', 'Key: ', find_word, 'Value: ', max_word)


file_handle.close()
