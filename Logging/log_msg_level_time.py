import logging


LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='debug_with_time_level_file.log', level=logging.DEBUG,
					format=LOG_FORMAT)
logger = logging.getLogger()

# test it here
logger.info('Test third message with level name and time include message itself')

print(logger.level)