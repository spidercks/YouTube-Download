#!/usr/python

import os
import time

os.system("clear")
os.system("pip install youtube_dl")
os.system("apt install figlet")
os.system("apt install jp2a")
os.system("clear")
print("\033[1;36;40m")
print("só mais um script do spider-pack")
os.system("figlet DownloadYT")

print("\033[1;33;40m")
print("[1] mp4\n")
print("[2] mp3\n")
print("\033[1;34;40m")
u_choice=int(input("--------> "))


if u_choice==1:

   print("Parâmetros inválidos 1\n")
   time.sleep(2)
   os.system("clear")
   os.system("python mp4.py")


if u_choice==2:
  
   print("Parâmetros inválidos 2\n")
   time.sleep(2)
   os.system("clear")
   os.system("python mp3.py")

print("by")
os.system("spiderckz")