"""
What is happening here is create a class and use with to create instance object
first create object and run the __eneter__ method display the msg
second the obj send the message run the text_msg()
thrid run the __exit__() methods display print msg
last run the last print msg to tell we are out of with statment
"""

class Student:

    def __enter__(self):
        print('We have entered "with" ')
        return self

    def __exit__(self, type, value, traceback):
        print('We are leaving "with" or exit of with')

    def text_msg(self):
        print('Hi, instance %s' % (id(self)))

# usually we create instance object like below
# obj = Student() but we use (with)


with Student() as obj:
    obj.text_msg()

print('After the "with" block')
