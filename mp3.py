


from __future__ import unicode_literals

import youtube_dl

import os

print("\033[1;32;40m")

os.system("clear")

print("\n\nMP3 Download\n\n")

os.system("jp2a yt.png")

print("\n\n")

u_url=input("Link do Vídeo: ")

ydl_opts = {

    'format': 'bestaudio/best',

    'postprocessors': [{

        'key': 'FFmpegExtractAudio',

        'preferredcodec': 'mp3',

        'preferredquality': '192',

    }],

}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    ydl.download([u_url])