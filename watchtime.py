import os
import time
import webbrowser
import pyautogui
import time
import socket # it helps to check Internet Coneection.
import subprocess # to run the cmd command.
from _thread import * # to run funtion in parallel.


ChannelButton = 'var ChannelForWatchTime = document.getElementsByClassName("style-scope ytd-channel-name");'
ChannelButtonClick = "ChannelForWatchTime[1].click();"
PlaylistButton = 'var Playlist = document.getElementsByClassName("style-scope ytd-button-renderer style-text size-default");'
PlaylistButtonClick = "Playlist[1].click();"  


i=0
print('''                                                                             
╔══╗    ╔╗               ╔═══╗          ╔╗      
╚╣╠╝    ║║               ║╔═╗║          ║║      
 ║║ ╔══╗║╚═╗╔══╗ ╔═╗     ║╚══╗╔╗╔═╗ ╔══╗║║ ╔══╗ 
 ║║ ║══╣║╔╗║║╔╗║ ║╔╗╗    ╚══╗║╠╣║╔╗╗║╔╗║║║ ║╔╗║ 
╔╣╠╗╠══║║║║║║╚╝╚╗║║║║    ║╚═╝║║║║║║║║╚╝║║╚╗║╚╝╚╗
╚══╝╚══╝╚╝╚╝╚═══╝╚╝╚╝    ╚═══╝╚╝╚╝╚╝╚═╗║╚═╝╚═══╝
                                    ╔═╝║        
                                    ╚══╝        

''')
print("Created by Ishan Singla\n")
br = int(input("choose your browser\n 1:chrome   2:-firefoxe   3:-internet explorer   4:-MS Edge\n  type(1,2,3,4):"))
w = int(input("\nhow many windows you want to open (recomended 10) :-"))
l= int (input("\nlength of video (minutes):- "))
l = l*60
name= input("\nName of channel: ")
link= "https://www.youtube.com/results?search_query="+name

if br==1 :
    b="chrome.exe"
elif br==2 :
    b="firefox.exe"
elif br==3 :
    b="iexplore.exe"
elif br==4 :
    b="msedge.exe"
else :
    print("Invalid! Input")
    time.sleep(2)

while (True) :
    if i<w :
        time.sleep(1)
        pyautogui.hotkey('win','r')
        time.sleep(0.5)
        pyautogui.typewrite(b, interval=0.02)
        pyautogui.hotkey('enter')
        time.sleep(2.0)
        pyautogui.hotkey('esc')
        time.sleep(2.0)
        pyautogui.typewrite(link, interval=0.02)
        pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.hotkey('f12')

        time.sleep(2)
        pyautogui.typewrite(ChannelButton)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite(ChannelButtonClick)
        pyautogui.press('enter')
        time.sleep(5)         
        pyautogui.typewrite(PlaylistButton)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite(PlaylistButtonClick)
        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.hotkey('f12')
        
        if br==2 :
        	pyautogui.hotkey('space')
        i += 1
        print("open window",i)
    elif i==w :
        i -= w
        time.sleep(l)
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im firefoxe.exe")
        os.system("taskkill /f /im iexplore.exe")
        os.system("taskkill /f /im msedge.exe")
        time.sleep(3)
    else :
        print ("Invalid input!")
        time.sleep(30)
