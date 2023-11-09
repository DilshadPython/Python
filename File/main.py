from urllib import request

goog_ulr = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=15&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'


def download_file_from_internet(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\n')

    save_url = r'google.csv'
    fwrite = open(save_url, 'w')
    for line in lines:
        fwrite.write(line + '\n')

    fwrite.close()

download_file_from_internet(goog_ulr)

# Very important note
# to make it work in your terminal run like below:
# python3 main.py
