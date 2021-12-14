# include libraries
# todo create class for keycode -> on key press jump to another mode which will record keypresses
# todo write saved commands into file
# todo load commands and run them


# text input end with 0 if 0 check for another shortcut to record
# import pyautogui as pt;
# docs : https://pynput.readthedocs.io/en/latest/index.html
from pynput import mouse, keyboard

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

# userCreatingData[2,{"s"}]
# class KeyboardPress:
#     def __init__(command,value):
#        command = ""
#        value = []
# key = KeyboardPress()


def firstLayout():
    # print(os.name())
    for i in sys.argv:
        print("system platform: " + i)
    # for i in platform.mac_ver():
    #     print(i)
    # print("source architecture: "+platform.mac_ver())
    userInput = input(
        "Press 'c' for create new routine or 'l' for load last routine\n")
    if(userInput == 'c'):
        dataCreate.dataCreate(userInput, mouse, keyboard)
        # mrelease
    elif(userInput == 'l'):
        load.loadData()
    else:
        print("Try valid char: 'c' or 'l' ")
        firstLayout()

# while(mouse.position!=(0,0)):
#     print('The current pointer position is %s' % format(mouse.position) )
#     sleep(0.3)
# print(pt.position())


firstLayout()
