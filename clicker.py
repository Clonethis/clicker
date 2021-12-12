# include libraries
# todo create class for keycode -> on key press jump to another mode which will record keypresses
#todo write saved commands into file
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

#loads data mode
import load
import keyboard
# creates data mode 
import create
# https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python

mouse = Controller()
tutorial = ["Press keys in :'' to make routine","'t' -> records text",
"'s' -> check for shortcut ends with '0'",
"'m' -> Left mouse click",
"'r' -> right mouse click"
"'d' -> deletes last command",
"'n' -> closes and saves data",
"'l' -> for write out all comands in this session",
"Program ends with mouse cursor on top left corner or by pressing: 'q'"
]
# mouse.position=(100,100)
# print('The current pointer position is ', format(mouse.position) )

# print(tutorial)
userInput = ""
# dict docs: https://www.w3schools.com/python/python_dictionaries.asp
# inputDict ={"s":damn(),"v":funct()}
userCreatingData=[()]
# userCreatingData[2,{"s"}]
# class KeyboardPress:
#     def __init__(command,value):
#        command = ""
#        value = []
# key = KeyboardPress()

def firstLayout():
    # print(os.name())
    for i in sys.argv:
        print("system platform: " +i)
    # for i in platform.mac_ver():
    #     print(i)
    # print("source architecture: "+platform.mac_ver())
    userInput = input("Press 'c' for create new routine or 'l' for load last routine\n")
    if(userInput=='c'):
        for i in tutorial:
            print(i)
        while(userInput!='q'):
            print("user Input : ",userInput)
            userInput= input("Press key:(t,s,d,m,r,n)")
            print("user Input2 after : ",userInput)
            if userInput=="r":
                # mouse.press(Button.right)
                # mouse.release(Button.right)
                pos = mouse.position
                userCreatingData.append(("r",pos))
                for i in userCreatingData:
                    print(f"userArray: {i}")
                # userCreatingData.append(["r"])
# generator docs; https://www.python.org/dev/peps/pep-0289/
                

                
                # print(pos)
                # userCreatingData.append(["r",pos])
                print("Right mouse click")
                # sleep(0.1)
            elif userInput=="c":
                for i in userCreatingData:
                    print(i)
        # print("saves nice")
        saveData(userCreatingData)
            # mrelease
    elif(userInput=='l'):
        # os.mkdir("saves")
        # https://www.tutorialspoint.com/python/os_listdir.htm
        if "saves" not in os.listdir("../clicker"):
            print("Try creating option first ")
            firstLayout()
        else:
            # print("Saved: '")
            print("\nWhich number would you like to run: ")
            for x, i in enumerate(os.listdir("saves")):
                i=i.split(".pkl")
                print(f"{x}: {i[0]}")
            # print("'")
            whichOne=input("")
            os.chdir("saves")        
            
            load.loadMode 
    else: 
        print("Try valid char: 'c' or 'l' ")
        firstLayout()
        
# while(mouse.position!=(0,0)):
#     print('The current pointer position is %s' % format(mouse.position) )
#     sleep(0.3)
# print(pt.position())

def saveData(arr):
    os.chdir("saves")
    userInput=input("Set name for save file: ")
    with open(userInput+".pkl", 'wb') as fh:
        pickle.dump(arr, fh)
    os.chdir("../")

firstLayout()