import time

def is_prime_v(num):
    if num == 1:
        return False   # 1 is not prime number

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

speed_0 = time.time()

for num in range(1, 29):
    print(num, is_prime_v(num))

speed_1 = time.time()

max_speed = speed_1 - speed_0
print('Speed need it: ', max_speed)