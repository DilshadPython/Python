'''
First install youtobe downloader
pip install youtube_dl
Refe:>> https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
'''
# https://www.youtube.com/watch?v=qODlKVzzeWs&list=RDqODlKVzzeWs&index=1
import youtube_dl

url = ['https://www.youtube.com/watch?v=-oQvMHpKkms&t=5193s']

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(url)
