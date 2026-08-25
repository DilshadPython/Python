
def out_side():
    # create local variable
    x = 'This is local var in out_side() called x'

    def in_side():
        nonlocal x
        # here print the x in_side function
        print(x)

    in_side()
    # here print the x out_side function
    print(x)

# we call the main function which is out_side()
out_side()
