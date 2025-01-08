# https://bookdepository.com/search?searchTerm=python&search=Find+book
from urllib.request import urlopen
from bs4 import BeautifulSoup

# pip install requests
import requests as rq

url = 'https://bookdepository.com/search?searchTerm=python&search=Find+book'

file = open('books.json', 'w')
resp = rq.get(url)

book_list = []
new_item = []

soup = BeautifulSoup(resp.content, 'html.parser')

for item in soup.findAll('', {'itemprop': 'name'}):
    new_item.append(item.get('content'))
book_list.append(new_item)

new_item = []
for item in soup.findAll('', {'itemprop': 'contributor'}):
    new_item.append(item.get('content'))
book_list.append(new_item)

for item in soup.findAll('', {'class': 'published'}):
    new_item.append(str(item)[-15:-4])
book_list.append(new_item)

file.write('{0:60} {1:25} {2:10}\n\n'.format(
    'Book name', 'Author', 'Publication Date'))

for i in range(len(book_list[0])):
    file.write('{0:60} {1:25} {2:10}\n'.format(
        book_list[0][i], book_list[1][i], book_list[2][i]))

file.close
