from pynput.mouse import Button, Controller
import keyboard

def routine(dataLoaded):
    mouse = Controller()
    print(f"loaded data: {dataLoaded}")
    for command in dataLoaded:
        # check for empty data, dunno, why they are in the code 
        if command == ():
            print("hey you")
        else:
            print(command)
            print(command[1])
        # if command[0] == "r":
        #     mouse.position(command[1])
        #     mouse.press(Button.right)
        #     mouse.release(Button.right)
        # else: 
        #     print("nothing")

