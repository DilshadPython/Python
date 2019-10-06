
c = 0  # This is counter

print("Press crtl and c")

try:
    while 1:  # infinite loop
        c += 1
except KeyboardInterrupt:
    print(f'The counter is {c} now')
