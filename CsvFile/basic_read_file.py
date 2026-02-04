
# This way is easy but maybe not safe
files = open('txtfile/basic.txt')
text = files.read()
files.close()

print(text)

# the better way is like below, because this way we don't need to close() at the end do it automatic
print('###' * 40)
with open('txtfile/dilshad_bio.txt') as f:
    bio = f.read()
    # we don't need to close the file here

print(bio)
