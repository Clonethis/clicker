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

#loads data mode
import load
import keyboard
# creates data mode 
import create
# https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python

mouse = Controller()
mpress = mouse.press(Button.left)
mrelease = mouse.release(Button.left)
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
        while(mouse.position!=(0,0) or userInput!='q'):
            userInput= input("Press key:(t,s,m,r,n)")
            if userInput=="s":
                # secondUserInput=input("")
                keyboard.key_recognizer()
            if userInput=="q":
                break
                    # userCreatingData.append(KeyboardPress("s",""))
            # if userInput=="t":
            #     secondUserInput=input("")
            #     while(secondUserInput!="0"):

            # elif userInput=="m":

            # elif userInput=="r":

            # elif userInput=="n":
            

    elif(userInput=='l'):
        if os.listdir("saves")==[]:
            print("Try creating option first ")
            firstLayout()

        print(os.listdir("saves"))
        whichOne=input("\nwhich should I run\n")
        os.chdir("saves")        
        load.loadMode 

# while(mouse.position!=(0,0)):
#     print('The current pointer position is %s' % format(mouse.position) )
#     sleep(0.3)
# print(pt.position())

def saveData(arr):
    os.chdir("saves")
    pickle.dumps(arr,"save1.txt")
    os.chdir("../")

firstLayout()