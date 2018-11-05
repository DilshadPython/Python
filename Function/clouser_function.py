def main():
    name = 'Dilshad Abdulla'
    address = '301 Hallmark Court'

    def submain():
        print('%s %s' % (name, address))

    return submain()


main()

print('###################################')


def first_func(name, address):
    detail = name + ' ' + address

    def second_func():
        print(detail)

    return second_func()

new_func = first_func('Tom Crus', 'London Road 12')

new_func
