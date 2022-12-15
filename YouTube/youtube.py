'''
First install youtobe downloader
pip install youtube_dl
Refe:>> https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
'''

import youtube_dl


# url = ['https://www.youtube.com/watch?v=yfgsklK_yFo&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy&index=1&t=19s&ab_channel=CodingEntrepreneurs']

url = ['https://www.youtube.com/watch?v=JPepam5D_BA&t=1127s&ab_channel=karwanhawleri']
with youtube_dl.YoutubeDL() as ydl:
    ydl.download(url)
