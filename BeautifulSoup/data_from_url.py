from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'http://www.bbc.co.uk/sport/football/tables'

file = open('football_team.txt', 'w')


i = 0

while i < 20:

    html_data = urlopen(url)
    soup = BeautifulSoup(html_data, 'html.parser')

    tableStats = soup.find('table', {'class': 'gs-o-table'})

    for row in tableStats.findAll('tr')[1:]:
        col = row.findAll('td')

        try:
            name = col[2].a.string.strip()
            # print(name)
            file.write(name + '\n')
        except:
            pass
    i += 20

file.close
