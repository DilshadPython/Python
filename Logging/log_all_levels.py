import logging


LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
## Notce when you change level=logging.INFO to any other level the number will change with output
logging.basicConfig(filename='log_all_levels.log', level=logging.DEBUG,
					format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()

# test it here
logger.info('First level info {}'.format(logger.level))
logger.debug('Second level debug {}'.format(logger.level))
logger.warning('Third level warning {}'.format(logger.level))
logger.error('Fourth level error {}'.format(logger.level))
logger.critical('Fifth level Critical {}'.format(logger.level))

print(logger.level)