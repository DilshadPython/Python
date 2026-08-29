class Book:

    @staticmethod
    def make_error():
        print('Entereting make_error()')
        # 5 make_error() ZeroDivisionError: division by zero
        8/0  # if you remove this line to error stop
        print('  leaving make_error()')

    def do_something(self):
        print('Entereting do_something() call >> make_error() to crate an Error')
        # 4 do_something() will call make_error() which is the privouse method
        # create an error by make_error() 8/0
        self.make_error()
        print(' leaving make_error()')


def some_util_func():
    print('Entering some_util_func() create obje and call obj.do_something()')
    # 3 some_util_func() create obj and obj.do_something(0 will be called)
    obj = Book()
    obj.do_something()
    print(' leaving some_util_func()')


def some_major_func():
    print('Entering some_major_func() call >> some_util_func()')
    # 2 some_major_fun() will call some_util_func()
    some_util_func()
    print(' leaving some_major_func()')


def main():
    print('Entering main() call >> some_major_func()')
    # when run the program 1 main() will be first which is call some_major_func()
    some_major_func() 
    print(' leaving main()')

try:
	main()
except ZeroDivisionError:
	print('Opps ....')
