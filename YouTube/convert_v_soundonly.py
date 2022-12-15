import moviepy.editor as mp

import tkinter.filedialog

video_f = openvideofile()
video_f = movieppy.editor.VideoFileClip(video_f)

audio = video_f.audio

audio.write_audiofile('Dlm Tanga.mp3')
print('success')