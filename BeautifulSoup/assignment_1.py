from bs4 import BeautifulSoup
# I am using python3 
import urllib.request


file = open('dilshad.txt', 'w')

data_list = []
new_item = []

with urllib.request.urlopen('https://www.squirrelsave.co.uk/') as url:
	soup = BeautifulSoup(url, 'html.parser')
	# soup = url.read() 

skip_link = soup.find('ul', id='skipLinks')
for link in skip_link.find_all('li'):
	new_item.append(link.a.string)
data_list.append(new_item)
# print(data_list)

new_item = []
current_header = soup.find('div', class_='discon-header')
header = current_header.p.text
new_item.append(header)
data_list.append(new_item)
# print(data_list)

new_item = []
# class is a key word in python to split with class in html need to add underscrow
navs = soup.find('ul', id='nav')
for nav in navs.find_all('li'):
	nav.a.text.split('\n')
	new_item.append(nav.a.text)
data_list.append(new_item)
# print(data_list)

new_item = []
main = soup.find('div', talign='center')
for content in main.find_all('p'):
	content.text.split('\n')
	new_item.append(content.text)
data_list.append(new_item)
# print(data_list)

new_item = []
footer_url = soup.find('div', id='footer')
for content in footer_url.find_all('li'):
	content.text.split('\n')
	new_item.append(content.text)
	for subcontent in content.find_all('a'):
		subcontent.text.split('\n')
		new_item.append(subcontent.text)
data_list.append(new_item)
print(data_list)

file.write('{0:35} {1:25} {2:40} \n\n'.format('URL', 'Title', 'Content'))

for x in range(len(data_list[0])):
	file.write('{0:35} {1:25} {2:40} \n'.format(
												data_list[0][x], 
												data_list[1][x], 
												data_list[2][x]												
												))

file.close
