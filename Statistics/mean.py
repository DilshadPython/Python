
import statistics as st

numbers = [6, 8, 29, 31, 0, 19, 27, 79, 12, 54, 24, 9, 4, 99, 12, 1, 3]

test_means = st.mean(numbers)

print('Mean is: ', test_means)

print('\n')
test_median = st.median(numbers)

print('Median is: ', test_median)

print('\n')
test_mode = st.mode(numbers)

print('Mode is: ', test_mode)

print('\n')
test_stdev = st.stdev(numbers)

print('Standard deviation: ', test_stdev)

print('\n')
test_veriance = st.variance(numbers)

print('Veriance is: ', test_veriance)
