'''
Prime Number: only divd by itself and 1
2, 3, 5, 7, 11, 13, 19, 19, 23

composite number: can be factored into small integer
4 = 2*2 or 6 = 2* 3, 9 = 3 * 3, 8 = 2* 4 or 8 = 2 * 2 *2 

Unit is 1
'''
import time


def is_prime(num):

	if num == 1:
		return (' is Unit = ', False)

	for i in range(2, num):
		if num % i == 0:
			return (' Not prime = ', False)
	return (' Yes is Prime = ', True)

start_time = time.time()
for i in range(1, 51):
	print(i, is_prime(i))

end_time = time.time()
print('The time is: ', end_time - start_time)