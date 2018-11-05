import logging
'''
1. we import students
2. run the file python login_basic.py 
3. the rsult will be only the student.log as out come from students.py the other file
   in login_basic has not be created because when we run the file which has the same
   line of code loggin.basicConfig  
'''
import students_1

'''
    We add another line below to change the debug level of the layout, this is 
    camelcase. the debug after level=logging.DEBUG is an integer run in background
    which is different than logging.DEBUG() , method which used logging.DEBUG(something)    
'''
logging.basicConfig(filename='output.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# first use debug
# second use info


def full_name():
    fname = 'Tom'
    lname = 'Alan'
    logging.info('Full name: ' + fname + ' ' + lname)


def address(street, city, postcode):
    return logging.info('Street: {} \nCity: {} \nPost Code: {}'.format(
        street,
        city,
        postcode)
    )


def contact(phone, email):
    logging.info('Phone: {} \nEmail: {}'.format(phone, email))


full_name()
address('6 Ursula Gould Way', 'E14 7FX', 'London')
contact('07825810648', 'info@gmail.com')
print('\n')
