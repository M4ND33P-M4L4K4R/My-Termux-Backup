####### MODULE #######
import os
import subprocess
import webbrowser
import random
import datetime
######################
#Greeting 
def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        os.system("termux-tts-speak Good Morning Sir")              
    elif hour >= 12 and hour <18:
        os.system("termux-tts-speak Good AfterNoon sir ")                   
    else:
        os.system("termux-tts-speak Good Evening Sir")
    os.system("termux-tts-speak I am Jarvis sir please Tell me How may I help You ") 
wishMe()
os.system("clear")

    
while True:
    colour = ["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m"]
    Colour=random.choice(colour)
    print()

    print(Colour," >>>>>[ Say Somthing...! ]<<<<")
    
    print()
    query = subprocess.getoutput("termux-speech-to-text")
    print()
    
    print("\033[41m""\033[32m[>",query, "<]\033[0m")

    
### Start 

    if "hello" in query or "Hi" in query:
        os.system("termux-tts-speak Hello Sir I am Jarvis")
        print("\033[34m""Hello Sir I am Jarvis ! \033[0m")

    elif "who are you" in query or "what is your name" in query:
        os.system("termux-tts-speak I am Jarvis Sir ")
        print("\033[38;5;209m"" I am Jarvis Sir")

    elif "game" in query or "which game" in query:
        os.system("termux-tts-speak You Play Free Fire")
# Caller         
    elif "call to my mother" in query or "call to my mom" in query:
        os.system("termux-tts-speak I am Calling sir ")
        os.system("termux-telephony-call 9199731523")
    elif "call to my father" in query or "call to my dad" in query:
        os.system("termux-tts-speak I am Calling sir ")
        os.system("termux-telephony-call 7464072850")
    elif "call to my brother" in query :
        os.system("termux-tts-speak I am Calling Sir ")
        os.system("termux-telephony-call 9939411504")
    elif "battery" in query or "status" in query:
        os.system("termux-tts-speak Here the Current information of your battery")
        os.system("termux-battery-status")
    elif "open Google" in query or "Google" in query:
        os.system("termux-tts-speak Opening Sir")
        os.system("termux-open-url https://google.com")
    elif "open YouTube" in query or "YouTube" in query :
        os.system("termux-tts-speak Opening Sir")
        os.system("termux-open-url https://YouTube.com")

    


    elif "play music" in query or "start music" in query or "music" in query : 
        os.system("bash music.sh")
# Termux-api command
    elif "torch" in query or "light" in query :
        os.system("termux-torch on")

    elif "vibrate" in query or "vibrate my device" in query:
        os.system("termux-tts-speak I am Vibrating Your device Sir")
        os.system("termux-vibrate")
    elif "contact list" in query :
        os.system("I am Listing your contact List")
        os.system("termux-contact-list")
    elif "brightness" in query :
        os.system("termux-tts-speak What should be the Ratio of brightness ")
        bright = subprocess.getoutput("termux-speech-to-text")
        print(str(bright))
        os.system("termux-brightness " + str(bright))
    elif "exit" in query or "stop" in query or "quit" in query :
        os.system("termux-tts-speak Okay Sir")
        exit()
    elif "Wi-Fi" in query:
        os.system("termux-tts-speak I am activating your wifi")
        os.system("termux-wifi-enable true")
    elif "disable Wi-Fi" in query :
        os.system("termux-tts-speak I am disactivated your wi-fi signal ")
        os.system("termux-wifi-enable true")
    elif "I love you" in query or "love" in query:
        os.system("termux-tts-speak I Love you too Sir")

    elif "search" in query or "find" in query :
        os.system("termux-tts-speak What do you wanna search For")
        print("\033[32m<<[ \033[33m""What Do You Wanna \033[31m\033[4mSEARCH \033[33mFor ? \033[32m]>>")
        print()
        command = subprocess.getoutput("termux-speech-to-text")
        print("\033[42m""\033[38;5;209m[>",command, "<]\033[0m")

        os.system("termux-open-url https://www.youtube.com/results?search_query=" + command)
        os.system("termux-tts-speak Here the Search Results About " + command + "From YouTube")
    elif "thanks" in query or "well done" in query:
        os.system("termux-tts-speak No problem Sir Its my pleasure ")

        # Tomorrow task 

    elif "task" in query or "desk" in query:
        os.system("termux-tts-speak Sir you have two task on Thursday 1 is Complete Notes of science maths and history....other is coding in bash python and in html and css. ......bye thank you sir ")
        



    else :
        os.system("termux-tts-speak Sorry sir ! i did not get that please Speak Again")
        print()
        print("\033[38;5;209m""Sorry sir ! i did not that please Speak Again !\033[0m ")


        

