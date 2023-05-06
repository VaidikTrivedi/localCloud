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