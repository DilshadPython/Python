import urllib.request 


req = urllib.request.urlopen('http://www.cashplusgroup.com/')

print(req.read())
