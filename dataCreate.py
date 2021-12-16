import pickle
import os
# import pynput.mouse
from pynput.mouse import Controller
import key
# from pynput.keyboard import Controller 

#Todo1 implement all functions bellow:

def shortcuts(array):
    keys =()
    keys = key.key_recognizer()
    array.append(("s",keys))
    #needs listner for keyboard events
    #live checks keyboard
    # returns 's' with tuple -> on press and on release value
    pass
def wait(array):
    #writes out whole current array
    array.append(("w",""))
def copy(array,buffer):
    # must set some global variable 'copybuffer' to some value selected by user 
    pass
def paste(array,buffer):
    # check if 'copybuffer' is not empty after that ctrl v 
    pass
def lMouseClick(array,mouse):
    # mouse = Controller()
    pos = mouse.position
    array.append(("l", pos))
    for i in array:
        print(f"userArray: {i}")

def rMouseClick(array,mouse):
    pos = mouse.position
    array.append(("r", pos))
    for i in array:
        print(f"userArray: {i}")
    print("Right mouse click")

def delete(array):
    #pops last element from array
    array.pop()
    
def close(array):
    pass
#todo2 pass them into adequate dataCreate if statements
#todo 3 in start.py
def dataCreate():
    mouse= Controller()
    keyboard = Controller()
    userCreatingData = [()]
    tutorial = ["Press keys in :'' to make routine", "'t' -> records text",
                "'s' -> check for shortcut ends with '0'or 'esc' key press",
                "'c' -> for copy -> same as ctrl+c"
                "'p' -> for paste -> same as ctrl+v"
                "'m' -> Left mouse click",
                "'r' -> right mouse click"
                "'d' -> deletes last command",
                "'n' -> closes and saves data",
                "'w' -> wait 1 sec",
                "Program ends with pressing: 'q'"
                ]
    userInput=""
    copyBuffer = ""
    for i in tutorial:
        print(i)
    while(userInput != 'q'):

        userInput = input("Press key:(t,s,d,m,r,n)")

        if   userInput == "s":
            shortcuts(userCreatingData)
        elif userInput == "r":
            rMouseClick(userCreatingData,mouse)
        elif userInput == "l":
            lMouseClick(userCreatingData,mouse)
        elif userInput == "w":
            wait(userCreatingData)
        elif userInput == "d":
            delete(userCreatingData)

        else:
            print("try valid key")
    print("running outside")
    saveData(userCreatingData)


def saveData(arr):
    # checks if folder 'saves' exists
    createFolder = True
    for i in os.listdir():
        if i == "saves":
            createFolder = False
            break
    if (createFolder):
        createMode()
    os.chdir("saves")
    userInput = input("Set name for save file: ")
    with open(userInput+".pkl", 'wb') as f:
        pickle.dump(arr, f)
    os.chdir("../")
    print("saved data successfuly")

def createMode():
    if (os.path.isdir("saves")):
        print("Saves folder already created")
        return 0;

    else:
        print("created saves")
        os.mkdir(path="saves")
