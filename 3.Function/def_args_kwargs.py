
def view(*args, **kwargs):
    print(args)
    print(kwargs)

view('Dilshad', 'Mohammed', stID=814747, age=45,
     university='Anglia Ruskin University')

print('\n##################################')
fullname = ['Shvan', 'Mohammed']
details = {'stID': 819847, 'age': 28, 'university': 'London University'}

view(fullname, details)

print('\n - See the different between this function how change the output:')

view(*fullname, **details)
