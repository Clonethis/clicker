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

# https://pypi.org/project/keyboard/

# loads data mode
import load


# creates file mode
import dataCreate
# https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python

mouse = Controller()
userInput = ""

def firstLayout():
    userInput = input("Press 'c' for create new routine or 'l' for load last routine\n")
    if(userInput == 'c'):
        dataCreate.dataCreate()
    elif(userInput == 'l'):
        load.loadData()
    else:
        print("Try valid char: 'c' or 'l' ")
        firstLayout()


firstLayout()
