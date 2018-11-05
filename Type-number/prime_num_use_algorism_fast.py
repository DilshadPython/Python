'''
Prime Number: only divd by itself and 1
2, 3, 5, 7, 11, 13, 19, 19, 23

composite number: can be factored into small integer
4 = 2*2 or 6 = 2* 3, 9 = 3 * 3, 8 = 2* 4 or 8 = 2 * 2 *2 

Unit is 1
'''
'''
36 = 1 * 36		18 = 1 * 18			num = 1 * num
	 2 * 18			 2 * 9				= a * b
	 3 * 12			 3 * 6				= ......
	 4 * 9

	 6 * 6								= ......
					 6 * 3				= b * a
	 9 * 4			 9 * 2				= num * 1
	 12 * 3			 18 * 1
	 18 * 2
	 36 * 1
	 
'''
import time
import math


def is_prime(num):

    if num == 1:
        return (' is Unit = ', False)

    # check is is even and not 2 then its nt prime
    if num == 2:
        return ('Yes is prime = ', True)
    if num > 2 and num % 2 == 0:
        return (' No prime = ', False)

    max_divition = math.floor(math.sqrt(num))

    for x in range(3, 1 + max_divition, 2):
        if num % x == 0:
            return 'No prime = ', False
    return ' Yes prime = ', True

start_time = time.time()
for num in range(1, 30000):
    print(num, is_prime(num))
end_time = time.time()
print('The time is: ', end_time - start_time)
