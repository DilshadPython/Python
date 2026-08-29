from bs4 import BeautifulSoup
import re

'''
	BeautifulSoup use to extract data from the web
'''
html_doc = """<html>
				<head>
					<title>Python 3.6 Tutorials</title>
				</head>
			<body>
				<h3 id='my-title' align='center'>Welcome to BeautifulSoup</h3>
				<title><b>I love Python</b></title>
				<p id='content-one' align='justify'>
					There are two variants of the installer: Miniconda is Python 2 based and Miniconda3 is Python 3 
					based. Note that the choice of which Miniconda is installed only affects the root environment. 
					Regardless of which version of Miniconda you install, you can still install both Python 2.x and 
					Python 3.x environments
					<small><a href='https://python.org/documents/</a>'</small>
				</p>

				<p id='content-two' align='justify'>
					There are two variants of the installer: Miniconda is Python 2 based and Miniconda3 is Python 3 
					based. Note that the choice of which Miniconda is installed only affects the root environment. 
					Regardless of which version of Miniconda you install, you can still install both Python 2.x and 
					Python 3.x environments
					<small><a href='https://python.org/documents/'</a></small>
				</p>

				<p id='content-three' align='justify'>
					There are two variants of the installer: Miniconda is Python 2 based and Miniconda3 is Python 3 
					based. Note that the choice of which Miniconda is installed only affects the root environment. 
					Regardless of which version of Miniconda you install, you can still install both Python 2.x and 
					Python 3.x environments
					<small><a href='https://python.org/documents/'</a></small>
				</p>

			</body>

		</html>"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.head)
print(soup.body.h3)
print(soup.body.title)
print(soup.body.small)
print(soup.body.p.a)

print('\n')
print('####' * 30)
print(soup.find_all('p'))
print(soup.find_all('a'))
print(soup.find_all('small'))
