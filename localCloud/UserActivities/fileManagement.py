import os
from pathlib import Path

def createDir(dirPath):
    currentPath = Path(__file__).parent.resolve()
    try:
        os.makedirs(os.path.join(currentPath._str + '//files//'+ dirPath))
        return True
    except Exception as e:
        print("Unable to create directory: "+ dirPath)
        print("StackTrace: ", e)
        raise Exception(e)
    
# TODO: find a way to return whole path of the image
def getItems(dirPath):
    currentPath = Path(__file__).parent.resolve()
    try:
        imageDir = os.listdir(os.path.abspath(os.path.join(currentPath._str + '//files//'+ dirPath)))
        return imageDir
    except Exception as e:
        print("Unable to get files: "+ dirPath)
        print("StackTrace: ", e)
        raise Exception(e)