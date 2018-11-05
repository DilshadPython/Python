from bs4 import BeautifulSoup
import urllib.request


req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')

# req = urllib.request.urlopen('http://www.findukphonenumber.com/numbers_beginning_with/0740002/')

xml = BeautifulSoup(req, 'xml')

for item in xml.findAll('link')[3:]:
    url = item.text
    news = urllib.request.urlopen(url).read()
    print(news)
