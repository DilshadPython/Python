def main():
    name = input('What is your name? ')
    # display = hi(name) print(display)
    print(hi(name))

# function has to return value or something print() is not return this is printsomething
def hi(msg='Python'):
    return f'Welcome back to, {msg}'

if __name__ == '__main__':
    main()