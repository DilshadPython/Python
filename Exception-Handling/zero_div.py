
def create_error():
    2/0


try:
    create_error()
except ZeroDivisionError as e:
    print('Error type is >> ', e)
   
