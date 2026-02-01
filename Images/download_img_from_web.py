import random
import urllib.request


def dwonload_img_from_website(url):
    num = random.randrange(1, 3)
    my_img = str(num) + '.jpg'

    return urllib.request.urlretrieve(url, my_img)


dwonload_img_from_website('https://pbs.twimg.com/profile_images/888308505727422465/Mrv_BBAy_400x400.jpg')
