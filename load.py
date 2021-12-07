import os
def loadMode(whichone):
    try:
        os.chdir("saves")
        fp = open(whichone+".txt")     
    except PermissionError:
        return "some default data"
    else:
        with fp:
            return fp.read()
