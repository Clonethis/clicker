import os
import pickle
# whichone is valid pkl file to open-> returns loaded data
def loadMode(whichone):
    try:
        # os.chdir("saves")
        fp = open(whichone,"rb")     
        
    except PermissionError:
        return "some default data"
    else:
        with fp as file_handle:
            data=pickle.load(file_handle)
            print(data)
        return data

            
