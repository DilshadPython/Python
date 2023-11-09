import urllib.request

url = input("https://www.youtube.com/watch?v=lnvmsohuTss \n")
name = input("My Baby Love \n")
name=name+".mp4"

try:
    print("Downloading starts...\n")
    urllib.request.urlretrieve(url, name)
    print("Download completed..!!")
except Exception as e:
    print(e)


urllib.request.urlretrieve(url_link, '') 
