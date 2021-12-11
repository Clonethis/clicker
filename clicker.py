# include libraries
# todo create class for keycode -> on key press jump to another mode which will record keypresses
#todo write saved commands into file
# todo load commands and run them



# text input end with 0 if 0 check for another shortcut to record
# import pyautogui as pt;
from pynput import mouse, keyboard
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
"Program ends with mouse cursor on top left corner or by pressing: 'q'"
]
# mouse.position=(100,100)
# print('The current pointer position is ', format(mouse.position) )

# print(tutorial)
userInput = ""
userCreatingData=[]
# class KeyboardPress:
#     def __init__(command,value):
#        command = ""
#        value = []
# key = KeyboardPress()

def firstLayout():
    userInput = input("Press 'c' for create new routine or 'l' for load last routine\n")
    if(userInput=='c'):
        for i in tutorial:
            print(i)
        while(userInput!='q'):
            print("user Input : ",userInput)
            userInput= input("Press key:(t,s,d,m,r,n)")
            print("user Input2 after : ",userInput)
            if userInput=="r":
                mouse.press(Button.right)
                mouse.release(Button.right)
                userCreatingData.append("r")

                print("Iran")
                sleep(0.1)
            elif userInput=="c":
                for i in userCreatingData:
                    print(i)
        saveData(userCreatingData)
            # mrelease
    elif(userInput=='l'):
        # os.mkdir("saves")
        # https://www.tutorialspoint.com/python/os_listdir.htm
        if "saves" not in os.listdir("../clicker"):
            print("Try creating option first ")
            firstLayout()
        else:
            print(os.listdir("saves"))
            whichOne=input("\nwhich should I run\n")
            os.chdir("saves")        
            
            load.loadMode 

# while(mouse.position!=(0,0)):
#     print('The current pointer position is %s' % format(mouse.position) )
#     sleep(0.3)
# print(pt.position())

def saveData(arr):
    savingString=""
    for i in arr:
        savingString+=i
    os.chdir("saves")
    pickle.dumps(arr,"save1.txt")
    os.chdir("../")

firstLayout()