import os
import pickle
import start
# loads data from file



def loadData():
    # os.mkdir("saves")
    # https://www.tutorialspoint.com/python/os_listdir.htm
    if "saves" not in os.listdir("../clicker"):
        print("Try creating option first ")
        return 0
    else:
        # print("Saved: '")
        print("\nWhich number would you like to run: ")
        for x, i in enumerate(os.listdir("saves")):
            i = i.split(".pkl")
            print(f"{x}: {i[0]}")
        # print("'")
        whichOne = input("")
        # os.chdir("saves")

        dataLoaded = loadMode(os.listdir("saves")[int(whichOne)])
        iteration = input("how many times would you like to run script?")
        input("on key press run selected routine")
        start.routine(dataLoaded,int(iteration))


def loadMode(whichone):
    try:
        os.chdir("saves")
        fp = open(whichone,"rb")
        new_dict = pickle.load(fp)
        fp.close()
        return new_dict
    except PermissionError:
        return "some default data"
