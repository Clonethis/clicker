import os
import clicker

# loads data from file


def loadMode(whichone):
    try:
        os.chdir("saves")
        fp = open(whichone+".pkl")
    except PermissionError:
        return "some default data"
    else:
        with fp:
            return fp.read()


def loadData():
    # os.mkdir("saves")
    # https://www.tutorialspoint.com/python/os_listdir.htm
    if "saves" not in os.listdir("../clicker"):
        print("Try creating option first ")
        clicker.firstLayout()
    else:
        # print("Saved: '")
        print("\nWhich number would you like to run: ")
        for x, i in enumerate(os.listdir("saves")):
            i = i.split(".pkl")
            print(f"{x}: {i[0]}")
        # print("'")
        whichOne = input("")
        os.chdir("saves")

        loadMode(whichOne)

