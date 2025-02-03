# we use _ for lname which is means we try to unpack here if don't put the lname
# it shows me an error because it has to be two value but if I enter both display
# the fname because this is what requested in print

fname, _ = input("What is your name? ").split(' ')
print(f"Welcome back, {fname}!")
