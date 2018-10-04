from bs4 import BeautifulSoup
# I am using python3 
import urllib.request


with urllib.request.urlopen('https://www.squirrelsave.co.uk/') as url:
	soup = BeautifulSoup(url, 'lxml')
	# soup = url.read() 

skip_link = soup.find('ul', id='skipLinks')

for link in skip_link.find_all('li'):
	print( 'Skipped content: ', link.text, ' | ', 'Skipped URLS: ', link.a)

print()

current_header = soup.find('div', class_='discon-header')
header = current_header.p.text
print('Page header: ', header)

print()

# class is a key word in python to split with class in html need to add underscrow
navs = soup.find('ul', id='nav')
for nav in navs.find_all('li'):
	print('Navbar: ', nav.a.text, ' | ', 'Nav URLS: ', nav.a)

print()

main = soup.find('div', talign='center')
print('Page content: ')
for content in main.find_all('p'):
	print(content.text, '\n')

print()

footer_url = soup.find('div', id='footer')
print('Page footer: ')
for content in footer_url.find_all('li'):
	print(content.text, '\n')
	for subcontent in content.find_all('a'):
		print('\t\t', subcontent.text, ' | ', 'URLS: ', subcontent)


