import math
import time

def is_prime_v3(num):
    # Return True if num is prime number, False if is not prime
    if num == 1:
        return False # 1 is not prime number

    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(num))

    for divisor in range(3, max_divisor + 1, 2):
        if num % divisor == 0:
            return False
    return True

speed_0 = time.time()
for num in range(1, 29):
    print(num, is_prime_v3(num))

speed_1 = time.time()
max_speed = speed_1 - speed_0

print('Speed need it: ', max_speed)