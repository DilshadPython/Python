import pickle


class PickleClass:

    def __init__(self, value, name):
        self.val = value
        self.name = name

    def increament(self):
        self.val += 1

    def lessonname(self):
        return self.name


obj = PickleClass(22, 'tutorials')
# obj_name = PickleClass('tutorial')

obj.increament()
obj.increament()
obj.lessonname()

print('To store data into the file enter 1 to read the data from file enter 2 :')
var = int(input('Enter 1 or 2: \n'))

if var == 1:
    with open('dataf.txt', 'wb') as file:
        pickle.dump(obj, file)
elif var == 2:
    with open('dataf.txt', 'rb') as file:
        unpickedobj = pickle.load(file)
        # print(unpickedobj)
        print(unpickedobj.val)
        print(unpickedobj.name)
else:
    pass
