from bs4 import BeautifulSoup
# import re

'''
	BeautifulSoup use to extract data from the web
'''
html_doc = """<html>
				<head>
					<title>Python 3.6 Tutorials</title>	
					<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
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
head_tag = soup.head
print('--Head--')
print(head_tag)

print('#################################################')
print(' ---- content in the head ---- ')
print(head_tag.contents)

print('#################################################')

title_tag = head_tag.contents[1]
print('')
print(' ---- Title ---- ')
print(title_tag)
print('==== title contents ====')
print(title_tag.contents)

print('')
print('==== length ====')
print(len(soup.contents))

print('')
print('Looping')
for sub in head_tag.descendants:
	print(sub)

title_tag = soup.title 
print(' parent titile')
print(title_tag.parent)
print(' ==== Display the top title ====')
print(title_tag.string.parent)

print('')
html_tag = soup.html
print(' ==== display parent ==== ')
print(html_tag.parent)
print(html_tag)

print('')
print(type(html_tag.parent))

print('')
print(' ==== soup.parent ==== ')
print(soup.parent)

print('')
link_tag = soup.a 
small_tag = soup.small 
print(' ==== find a tage and script tag ==== ')
print(link_tag)
print(small_tag)

print(' ==== name of all tags has been used in the html ==== ')
for parent in link_tag.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)

