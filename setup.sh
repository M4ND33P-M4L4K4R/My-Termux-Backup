#!/bin/bash  
#termux-open-url https://play.google.com/store/apps/details?id=com.termux.api  

clear
echo -e "\033[32m>>>[ Script Process Started Keep Internet on ]<<<"
sleep 2
echo -e "\033[33m"
echo -e "Make Sure that You Have already install \033[34m.   \n.        Termux-api \033[33m\n.       From Playstore\n\033[32mOtherwise Install it with playStore "
sleep 7
termux-open-url https://play.google.com/store/apps/details?id=com.termux.api
apt update 
apt upgrade 
pkg install termux-api -y 
pkg install lolcat -y
echo -e "\033[36m"
pkg install figlet -y 
plg install mpv -y 
pkg install python -y 
pkg install python2 -y
pkg install termux-api -y 
pip install webbrowser
pip install colorama 
pip install datetime
pip install random 
pip install subprocess 
pip install os 
echo -e "\033[38;5;209m"
figlet Done! | lolcat
sleep 4
echo -e "\033[38;5;223mAll Requirements is satisfied"
termux-setup-storage
cd MY_PERSONAL_ASSISTANT
ls 
chmod +x * 
clear 
echo -e "\033[34m .......[ Please Wait ].........."
python Assistant.py 


