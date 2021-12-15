from pynput.mouse import Button, Controller
# import keyboard
#read commands from file, create adequate functions

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
def lMouseClick(array):
    #same as rMouseClick
    pass
def rMouseClick(array):
    pass
def delete(array):
    #pops last element from array
    pass
def close(array):
    pass
from collections import deque
from time import sleep
def routine(dataLoaded):
    # there you can change time between each command
    defaultSleep = 1
    mouse = Controller()
    print(f"loaded data: {dataLoaded}")
    for command in dataLoaded:
        # check for empty data, dunno, why they are in the code 
        if command == ():
            # print("hey you")
            pass
        else:
            value = command[1]
            command = command[0]
            # print(command)
            # print(command[1])
            if command == "r":
                mouse.position = value
                mouse.press(Button.right)
                mouse.release(Button.right)
                sleep(defaultSleep)
            if command == "l":
                mouse.position = value
                mouse.press(Button.left)
                mouse.release(Button.left)
                sleep(defaultSleep)

        # else: 
        #     print("nothing")

