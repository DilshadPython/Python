import math
import time

def is_prime_v2(num):
    # Return True if num is prime number, False if is not prime
    if num == 1:
        return False # 1 is not prime number
    max_divisor = math.floor(math.sqrt(num))

    for divisor in range(2, max_divisor + 1):
        if num % divisor == 0:
            return False
    return True

speed_0 = time.time()
for num in range(1, 29):
    print(num, is_prime_v2(num))

speed_1 = time.time()
max_speed = speed_1 - speed_0
print('Speed need it: ', max_speed)