#!/usr/bin/python2

import os 


#Variable
command = str(input("Enter your command : "))
if command == "speak":
    os.system("termux-tts-speak")
elif command == "listen" :
    os.system("termux-speech-to-text")
else:
    print("Sorry sir There doesn\'t exist this type of File!")





