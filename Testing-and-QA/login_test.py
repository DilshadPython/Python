import logging


print('Please enter info, debug warning')

msg = input('Select the logging type: \n')

if msg == 'info':
	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")
elif msg == 'debug':
	logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
elif msg == 'warning':
	logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(levelname)s:%(message)s")
else:
	print('logging not in the list above')

logging.debug('This is debug will be ignored')
logging.info('This is should be logged')
logging.warning('And this too....')