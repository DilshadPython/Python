from commands import lnx_list


# try:
for key in lnx_list.items():
    key = str(input('Enter the command name: '))
    if key in lnx_list:
        print(key, ' : ', lnx_list[key], '\n')

    else:
        print('The key you enterted is not exisit')
