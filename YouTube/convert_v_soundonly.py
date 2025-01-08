import moviepy.editor as mp

import tkinter.filedialog

video_f = openvideofile('My Baby Love song popular music in YouTube-lnvmsohuTss.mp4')
video_f = movieppy.editor.VideoFileClip(video_f)

audio = video_f.audio

audio.write_audiofile('My Baby Love.mp3')
print('success')