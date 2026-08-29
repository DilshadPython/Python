import requests

r = requests.get('https://www.teach-cloud.net/cms/about/')

# the output must be <Response [200]>
print(r)
print(r.status_code)

a = requests.get('https://www.teach-cloud.net/cms/projects/')
print(a.url)

# See whatelse we can use
print(dir(r))
print('Links')
print(r.links)

# More informations
# print(help(r))

#display html
# print(r.text)

# download an image from the page
x = requests.get('https://www.teach-cloud.net/static/profile/dilshad-abdulla.jpeg')

with open('da.jpeg', 'wb') as f:
     f.write(x.content)

# General informations http status codes
'''
200 are success
300 is redirect
400 is client error 
500 is server error 
'''

myurl = 'https://www.teach-cloud.net/static/profile/dilshad-abdulla.jpeg'

y = requests.get(myurl)
# display 200
print(y.status_code)


print(y.ok)

# this is a header of this page
print('Header contents:')
print(y.headers)

# This links https://www.httpbin.org/ is display and test different methods

# create a dictionary to get this info from the link below
myload = {
     'page': 2,
     'count': 25
}

z = requests.get('https://httpbin.org/get', params=myload)
print(z.text)
print(z.url)

mydata = {
     'username': 'hello',
     'password': 'passy',
}

c = requests.post('https://httpbin.org/post', data=mydata)

print(c.text)
# Here we will print as json object
print('Display json object:')
print(c.json())

# Or if we want to display as dictionary
print('Display as dict')
c_dict = c.json()
print(c_dict['form'])

'''
If we rung this linke https://www.httpbin.org/basic-auth/hello/passy
the server will display a login page.
'''

# We are display the username and password as dictionary
print('\nDisplay the username and password:')
d = requests.get('https://httpbin.org/basic-auth/hello/passy', auth=('hello', 'passy'))
print(d.text)

# TO show an error like add username wrong
print('\nDisplay an error like 401 which is mean unauthorized username or password:.')
e = requests.get('https://httpbin.org/basic-auth/hello/passy', auth=('george', 'passy'))
print(e)
print('\nDisplay an authorized username or password:.')
f = requests.get('https://httpbin.org/basic-auth/hello/passy', auth=('hello', 'passy'))
print(f)

 # Display the username and password with the time setup
print('\nDisplay an authorized username or password:.')
g = requests.get('https://httpbin.org/delay/5', timeout=5)
print(g)

#
print('\nDisplay an authorized before the 5 second:')
h = requests.get('https://httpbin.org/delay/4', timeout=5)
print(h)

print('\nDisplay an authorized after the 5 second which is an Error:')
i = requests.get('https://httpbin.org/delay/6', timeout=5)
print(i)