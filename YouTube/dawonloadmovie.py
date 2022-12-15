import urllib.request

url = input("https://w3.yesmovies123.me/movies/queen-of-hearts/ \n")
name = input("Queen of Heart \n")
name=name+".mp4"

try:
    print("Downloading starts...\n")
    urllib.request.urlretrieve(url, name)
    print("Download completed..!!")
except Exception as e:
    print(e)


urllib.request.urlretrieve(url_link, '') 
