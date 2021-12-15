import pickle
import os
# import pynput.mouse
from pynput.mouse import Controller, Button

#Todo1 implement all functions bellow:

def shortcuts(array):
    #live checks keyboard
    # returns 's' with tuple -> on press and on release value
    pass
def listArray(array):
    #writes out whole current array
    pass
def copy(array,buffer):
    # must set some global variable 'copybuffer' to some value selected by user 
    pass
def paste(array,buffer):
    # check if 'copybuffer' is not empty after that ctrl v 
    pass
def lMouseClick(array,mouse):
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
    pass
def close(array):
    pass
#todo2 pass them into adequate dataCreate if statements
#todo 3 in start.py
def dataCreate():
    mouse= Controller()
    userCreatingData = [()]
    tutorial = ["Press keys in :'' to make routine", "'t' -> records text",
                "'s' -> check for shortcut ends with '0'or 'esc' key press",
                "'c' -> for copy -> same as ctrl+c"
                "'p' -> for paste -> same as ctrl+v"
                "'m' -> Left mouse click",
                "'r' -> right mouse click"
                "'d' -> deletes last command",
                "'n' -> closes and saves data",
                "'l' -> for write out all comands in this session",
                "Program ends with pressing: 'q'"
                ]
    userInput=""
    for i in tutorial:
        print(i)
    while(userInput != 'q'):
        userInput = input("Press key:(t,s,d,m,r,n)")

        if userInput == "r":
            rMouseClick(userCreatingData,mouse)
            # sleep(0.1)
        elif userInput == "l":
            lMouseClick(userCreatingData,mouse)
        elif userInput == "c":
            for i in userCreatingData:
                print(i)
    print("running outside")
    saveData(userCreatingData)


def saveData(arr):
    # checks if folder 'saves'
    createFolder = True
    for i in os.listdir():
        if i == "saves":
            createFolder = False
            break
    if (createFolder):
        createMode()
    os.chdir("saves")
    userInput = input("Set name for save file: ")
    with open(userInput+".pkl", 'wb') as fh:
        pickle.dump(arr, fh)
    os.chdir("../")

def createMode():
    if (os.path.isdir("saves")):
        print("Saves folder already created")
        return 0;

    else:
        print("created saves")
        os.mkdir(path="saves")
