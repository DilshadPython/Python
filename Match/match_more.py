keyword = input("Enter the keywords are available in Python? ")

match keyword:
    case 'print' | 'elif' | 'for' | 'while' | 'break' | 'continue' | 'raise' | 'def':
        print('is Python')
    case _:
        print('is not clear')