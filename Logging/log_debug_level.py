
import logging

logging.basicConfig(filename='debugfile.log', level=logging.DEBUG)
logger = logging.getLogger()

# test it here
logger.info('Test second message with level of debug')

print(logger.level)
