from pynput.mouse import Button, Controller
import keyboard
from time import sleep
def routine(dataLoaded):
    defaultSleep = 1
    mouse = Controller()
    print(f"loaded data: {dataLoaded}")
    for command in dataLoaded:
        # check for empty data, dunno, why they are in the code 
        if command == ():
            print("hey you")
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
        # else: nic
        #     print("nothing")

