'''
First install youtobe downloader
pip install youtube_dl
'''

import youtube_dl


# url = ['https://www.youtube.com/watch?v=cFdApmqlllg&t=933s&ab_channel=%D9%86%D9%88%D8%A7%DB%8C%D8%A7%DB%8C%D8%B1%D8%A7%D9%86']
# url = ['https://www.youtube.com/watch?v=8ynhZ7Qj1As&ab_channel=MohammadMamleOfficialPage']
url = ['https://www.youtube.com/watch?v=HcneMCAeU_g&list=RDMMHcneMCAeU_g&start_radio=1&ab_channel=AhmadGoran']
with youtube_dl.YoutubeDL() as ydl:
    ydl.download(url)
