import logging
import math


LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
# Notce when you change level=logging.INFO to any other level the number
# will change with output
logging.basicConfig(filename='log_math.log', level=logging.DEBUG,
                    format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()

# test it here
logger.info('First level info {}'.format(logger.level))
logger.debug('Second level debug {}'.format(logger.level))
logger.warning('Third level warning {}'.format(logger.level))
logger.error('Fourth level error {}'.format(logger.level))
logger.critical('Fifth level Critical {}'.format(logger.level))

print(logger.level)


def quadratic_formula(a, b, c):
    ''' Test the solution to the equation ax^2 + bx + c = 0. '''
    logger.info('quadratic_formula({0}, {1}, {2}'.format(a, b, c))

    # compute the discriminant
    logger.debug(' # Compute the discriminant')
    disc = b**2 - 4 * a * c

    # compute the two roots
    logger.debug(' # Compute the two roots')
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b + math.sqrt(disc)) / (2 * a)

    # return the roots
    logger.debug('# Return the roots')
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)
