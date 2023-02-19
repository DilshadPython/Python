import pickle

temas = ['Manchester U', 'Aresenal', 'Man City',
         'Liverpool', 'Chelsea', 'Tottenham']

print('To store data into the file enter a to read the data from file enter b :')
var = str(input('Enter a or b: \n'))

if var == 'a':
    with open('teamdata.txt', 'wb') as tmd:
        pickle.dump(temas, tmd)
elif var == 'b':
    with open('teamdata.txt', 'rb') as tmd:
        unpickledteam = pickle.load(tmd)
        print(unpickledteam)
else:
    print('Enter valid var, you you entered wrong variable')

