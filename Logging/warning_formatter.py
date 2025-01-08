import logging

'''
    We add another line below to change the debug level of the layout, this is 
    camelcase. the debug after level=logging.DEBUG is an integer run in background
    which is different than logging.DEBUG() , method which used logging.DEBUG(something)    
'''
logging.basicConfig(filename='format.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


def full_name():
    fname = 'Tom'
    lname = 'Alan'
    logging.warning('Full name: ' + fname + ' ' + lname)


def address(street, city, postcode):
    return logging.warning('Street: {} \nCity: {} \nPost Code: {}'.format(street, city, postcode))


def contact(phone, email):
    logging.warning('Phone: {} \nEmail: {}'.format(phone, email))


full_name()
address('6 Ursula Gould Way', 'E14 7FX', 'London')
contact('07825810648', 'info@gmail.com')
print('\n')
