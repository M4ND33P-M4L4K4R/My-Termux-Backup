#!/usr/bin/python2 
import os 
os.system("find -L /sdcard -type f -ipath '*.mp3' >mp3.list")
os.system("find -L /storage/sdcard1 -type f -ipath '*.mp3' >>mp3.list")



print("\033[33m"" Scan Complete sir")
