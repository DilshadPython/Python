keep_going = True
a = 0
b = 0
while keep_going:
    print("O")
    if a + b >= 24:
        keep_going = False
    a = a + 5
    b = b + 7
