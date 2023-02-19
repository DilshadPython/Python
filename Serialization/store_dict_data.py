import pickle

number = 666

message = 'Hello Python tutorials'

mydict_list = {
	'a': ['Python', 'Django', 'Flask', 'Java'],
	'b': [10, 25, 33, 4],
	'c': [101, 201, 301, 401]
}

query_output = [('Dill', 'Tom', 25, 'Sam'), ('Python', 'version', 3.10, 'tutorilas')]


print('To store data into the file enter 1 to read the data from file enter 2 :')
var = int(input('Enter 1 or 2: \n'))

if var == 1:
	# we store the multi different data to the file
    with open('dictdata.txt', 'wb') as tmd:
        pickle.dump((number, message, mydict_list, query_output), tmd)
elif var == 2:
	# read the data from the file
    with open('dictdata.txt', 'rb') as tmd:
        tupledata = pickle.load(tmd)
        print(tupledata[0])
        print(tupledata[1])
        print(tupledata[2])
        print(tupledata[3])
        print(tupledata)
else:
    print('Enter valid var, you you entered wrong variable')

