

students_name = {
    '0814747': 'Dilshad Abdulla',
    '0814572': 'Alna Shira',
    '0859863': 'Clear Mitchell',
    '0813562': 'Rachel Soll',
}


def get_id():
    stdid = None
    print('Please enter the rquirements:')
    id = input('Please enter the id number: ')
    if id is True:
        return 'Hi %s' % students_name.get(id, ' registered')
    else:
        result = 'Sorry this {} not registered!!'.format(id)
        return result

get_id()
