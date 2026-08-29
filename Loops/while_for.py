while True:
    n = int(input('Wht is the n number? '  ))
    # if you enter a negative number repeate the question
    if n > 0:
        break # choose key for completion

for _ in range(n):
    print(f'Welcome to while for loop {n} times!') #.format(n=n)
