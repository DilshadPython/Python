def get_prime_factors(start, end):
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num

print(list(get_prime_factors(1, 100)))
