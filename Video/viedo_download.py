import requests

def downloadfile(name, url):
    name = name+".mp4"
    r = requests.get('url')
    print("****Connected****")
    f = open(name,'http://www.incestflix.com/watch/queen-of-hearts-2019-dronningen');
    print("Donloading.....")
    for chunk in r.iter_content(chunk_size=255): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    print("Done")
    f.close()