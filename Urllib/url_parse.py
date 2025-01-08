import urllib.request
import urllib.parse


values = {'q': 'Martina Salvatore'}

data = urllib.parse.urlencode(values)

url = 'https://www.google.com/search?' + data

# data = data.encode('utf-8')

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
resp_data = resp.read()
print(resp_data)
