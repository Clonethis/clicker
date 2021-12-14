import create
import pickle
import os


def dataCreate(userInput, mouse, keyboard):
    # dict docs: https://www.w3schools.com/python/python_dictionaries.asp
    # inputDict ={"s":damn(),"v":funct()}
    userCreatingData = [()]

    tutorial = ["Press keys in :'' to make routine", "'t' -> records text",
                "'s' -> check for shortcut ends with '0'",
                "'m' -> Left mouse click",
                "'r' -> right mouse click"
                "'d' -> deletes last command",
                "'n' -> closes and saves data",
                "'l' -> for write out all comands in this session",
                "Program ends with mouse cursor on top left corner or by pressing: 'q'"
                ]
    for i in tutorial:
        print(i)
        while(userInput != 'q'):
            print("user Input : ", userInput)
            userInput = input("Press key:(t,s,d,m,r,n)")
            print("user Input2 after : ", userInput)
            if userInput == "r":
                # mouse.press(Button.right)
                # mouse.release(Button.right)
                pos = mouse.position
                userCreatingData.append(("r", pos))
                for i in userCreatingData:
                    print(f"userArray: {i}")
                # userCreatingData.append(["r"])
                # generator docs; https://www.python.org/dev/peps/pep-0289/

                # print(pos)
                # userCreatingData.append(["r",pos])
                print("Right mouse click")
                # sleep(0.1)
            elif userInput == "c":
                for i in userCreatingData:
                    print(i)
        # print("saves nice")
        for i in os.listdir():
            print("dir: i: "+i)
        # print("list dir: "+os.listdir())
        saveData(userCreatingData)


def saveData(arr):
    # checks if folder 'saves'

    if (not os.isdir("saves")):
        create.createMode()
    os.chdir("saves")
    userInput = input("Set name for save file: ")
    with open(userInput+".pkl", 'wb') as fh:
        pickle.dump(arr, fh)
    os.chdir("../")
