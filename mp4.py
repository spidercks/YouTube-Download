from __future__ import unicode_literals
import youtube_dl
import os

print("\033[1;31;40m")
os.system("clear")
print("\n\nmp4 downloader\n\n")
os.system("jp2a yt.png")
print("\n\n")
u_link=input("Link do video: ")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([u_link])