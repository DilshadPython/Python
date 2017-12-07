
from statistics import median, stdev

numbers = [6, 8, 29, 31, 0, 19, 27, 79, 12, 54, 24, 9, 4, 99, 12, 1, 3]

test_median = median(numbers)

print('Median is: ', test_median)

test_stdev = stdev(numbers)

print('Stdev is: ', test_stdev)
