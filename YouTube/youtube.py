'''
First install youtobe downloader
pip install youtube_dl
Refe:>> https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
'''

import youtube_dl

url = ['https://www.youtube.com/watch?v=HcneMCAeU_g&list=RDMMHcneMCAeU_g&start_radio=1&ab_channel=AhmadGoran']

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(url)
