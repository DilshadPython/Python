import logging


def full_name():
	fname = 'Dilshad'
	lname = 'Abdulla'
	logging.warning('Full name: ' + fname + ' ' + lname)

def address(street, city, postcode):
	return logging.warning('Street: {} \nCity: {} \nPost Code: {}'.format(street, city, postcode))

def contact(phone, email):
	logging.warning('Phone: {} \nEmail: {}'.format(phone, email))


full_name()
address('6 Ursula Gould Way', 'London', 'E14 7FX')
contact('07825810648', 'info@gmail.com')
