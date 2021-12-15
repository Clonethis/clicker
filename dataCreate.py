import pickle
import os


def dataCreate(mouse, keyboard):
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
            userInput = input("Press key:(t,s,d,m,r,n)")

            if userInput == "r":
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
    