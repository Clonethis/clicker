# include libraries
# todo create class for keycode -> on key press jump to another mode which will record keypresses
# todo write saved commands into file
# todo load commands and run them


# text input end with 0 if 0 check for another shortcut to record
# import pyautogui as pt;
# docs : https://pynput.readthedocs.io/en/latest/index.html
# from typing import Match

from pynput import mouse, keyboard
from collections import deque

# callable funct
# from typing import Set, List, Tuple, Dict, Callable
# docs:https://docs.python.org/3/library/sys.html#sys.platform
import sys

# import platform
from pynput.mouse import Button, Controller


# from pynput.keyboard import Key, Controller

from time import sleep
import os
import pickle
import keyboard
# https://pypi.org/project/keyboard/

# loads data mode
import load
import keyboard

# creates file mode
import create
import dataCreate
# https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python

mouse = Controller()
# mouse.position=(100,100)
# print('The current pointer position is ', format(mouse.position) )

# print(tutorial)
userInput = ""


def firstLayout():
    for i in sys.argv:
# <<<<<<< HEAD
#         print("system platform: " +i)
#     # for i in platform.mac_ver():
#     #     print(i)
#     # print("source architecture: "+platform.mac_ver())
#     userInput = input("Press 'c' for create new routine or 'l' for load last routine\n")
#     if(userInput=='c'):
#         for i in tutorial:
#             print(i)
#         while(userInput!='q'):
#             print("user Input : ",userInput)
#             userInput= input("Press key:(t,s,d,m,r,n)")
#             print("user Input2 after : ",userInput)
#             if userInput=="r":
#                 # mouse.press(Button.right)
#                 # mouse.release(Button.right)
#                 pos = mouse.position
#                 userCreatingData.append(("r",pos))
#                 for i in userCreatingData:
#                     print(f"userArray: {i}")
#                 # userCreatingData.append(["r"])
# # generator docs; https://www.python.org/dev/peps/pep-0289/
                

                
#                 # print(pos)
#                 # userCreatingData.append(["r",pos])
#                 print("Right mouse click")
#                 # sleep(0.1)
#             elif userInput=="c":
#                 for i in userCreatingData:
#                     print(i)
#         # print("saves nice")
#         saveData(userCreatingData)
#             # mrelease
#     elif(userInput=='l'):
#         # os.mkdir("saves")
#         # https://www.tutorialspoint.com/python/os_listdir.htm
#         if "saves" not in os.listdir("../clicker"):
#             print("Try creating option first ")
#             firstLayout()
#         else:
#             # print("Saved: '")
#             fInSaves = os.listdir("saves")

#             if(fInSaves==1):
#                 loadMode(os.listdir("save"))
#             else:
#                 print("\nWhich number would you like to run: \n")
#                 for x, i in enumerate(fInSaves):
#                     i=i.split(".pkl")
#                     print(f"{x}: {i[0]}")

#                 # print("'")
#                 whichOne=input("")
                

#                 os.chdir("saves")        

#                 loadedDate = load.loadMode(fInSaves[int(whichOne)])
                
#     else: 
# =======
        print("system platform: " + i)

    userInput = input(
        "Press 'c' for create new routine or 'l' for load last routine\n")
    if(userInput == 'c'):
        dataCreate.dataCreate(userInput, mouse, keyboard)
        # mrelease
    elif(userInput == 'l'):
        load.loadData()
    else:
        print("Try valid char: 'l' or 'l' ")
        firstLayout()


firstLayout()
