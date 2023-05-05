def main():
    name = input('Enter a name: ')
    # here we gave an arg but nothing given in the fun line 10 is only to
    # show how the function work is done it for test there is a bug which
    # is hello(name)
    hello(name)


def hello():
    print('Hello, ', name)


main()
