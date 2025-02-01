# uppercase var is a constants method you can not change it
class User:
    NAME = 'Dilshad'
    ADDRESS = 'Shenfield Road, Brentwood'

    def detail(self):
        print(self.NAME)
        print(self.ADDRESS)

user = User()
user.detail()

# Now we try to change the name and address but we can't
NAME = 'Tom'
ADDRESS = 'Jack Road, London'
user.detail()