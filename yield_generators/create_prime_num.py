def create_prime_list():
    # create an empty list
    prime_list = []
    for num in range(2, 100):
        if num % 2 == 0:
            prime_list.append(num)
    return prime_list
print(create_prime_list())


# create a not prime number
def create_no_prime_list():
    no_prime_list = []
    for num in range(2, 100):
        if num % 2 == 1:
            no_prime_list.append(num)
    return no_prime_list
print(create_no_prime_list())