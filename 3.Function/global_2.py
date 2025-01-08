x = 'Global x'

def out_side():

    def in_side():
        print(x)

    in_side()
    # here print the x out_side function
    print(x)

# we call the main function which is out_side()
out_side()
print(x)

