from bs4 import BeautifulSoup
import re

input = """<html>
				<head>
					<title>Bootstrap</title>
				</head>
			<body>
				<h3 id='my-title' align='center'>Welcome to BeautifulSoup</h3>
				<p id='content-one' align='justify'>
					Then, you can install things for Python 3.2 with pip-3.2, and install things for Python 2-7 
					with pip-2.7. The pip command will end up pointing to one of these, but I'm not sure which, 
					so you will have to check.
					<small>Date</small>
				</p>

				<p id='content-two' align='justify'>
					Then, you can install things for Python 3.2 with pip-3.2, and install things for Python 2-7 
					with pip-2.7. The pip command will end up pointing to one of these, but I'm not sure which, 
					so you will have to check.
					<small>Month</small>
				</p>

				<p id='content-three' align='justify'>
					Then, you can install things for Python 3.2 with pip-3.2, and install things for Python 2-7 
					with pip-2.7. The pip command will end up pointing to one of these, but I'm not sure which, 
					so you will have to check.
					<small>Year</small>
				</p>

			</body>

		</html>"""

soup = BeautifulSoup(input, 'lxml')
titleTage = soup.html.head.title 
print(titleTage)

print(titleTage.string)

print(len(soup('p')))

print(soup('p', {'align': 'justify'}))
print('')
print(soup('p', {'align': 'justify'})[0]['id'])

print(soup('p')[1].small.string)
print(soup('p')[2].small.string)
print(soup('p')[0].small.string)

titleTage['id'] = 'AngularJs'
#overwritten the title
titleTage.string = 'Django Framework'

print('=== Title & Content ===')
print(soup.html.head.title)
print(soup.html.head.title.contents)

