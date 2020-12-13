'''
First install youtobe downloader
pip install youtube_dl
'''

import youtube_dl


url = ['https://www.youtube.com/xxxxxx']

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(url)
