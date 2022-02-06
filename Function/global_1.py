x = 'Global x'

def out_side():

    def in_side():
        x = 'in side x'
        # here print the x in_side function
        print(x)

    in_side()
    # here print the x out_side function
    print(x)

# we call the main function which is out_side()
out_side()
print(x)

