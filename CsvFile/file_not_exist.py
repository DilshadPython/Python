
try:
    with open('txtfile/file_not_exisit.txt') as f:
        text = f.read()
except FileNotFoundError:
    text = None
    print('\n\tFile Not Exist')

print('\t',text)
