'''
'Using Try to count from 1 to when the user press ctrl and c on the keyboard,
 after we will see how many number has been counted until ctrl+c entered
'''
c = 0  # This is counter

print("Press crtl and c")

try:
    while 1:  # infinite loop
        c += 1
except KeyboardInterrupt:
    print(f'The counter is {c} now')
