import os
def createMode():
    if (os.path.isdir("saves")):
        print("Saves folder already created")
        return 0;

    else:
        print("created saves")
        os.mkdir(path="saves")
    