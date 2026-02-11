# to test for non python take one num out of the list else works
num_list = [6, 5, 8, 1, 8, 9, 3] # to test for non pythonic remove one num
# try option is much more pythonic because doesn't ask for remove or add any num automatically test and display
# the results if True or False the len index

# if len(num_list) >= 7:
#     # correct
#     # but if the length doesn't match for example take one num out of the list the else execute
#     for num in num_list:
#         print(num)
#     print(num_list[6])
# else:
#     print("The index length does not exist")

# Pythonic
try:
    print(num_list[6], " The len is correct!")
except IndexError:
    print("The index doesn't exist")