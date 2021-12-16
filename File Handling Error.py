# file handling error

import os

try:
    os.mkdir("/Users/karpuri/Desktop/1234567")
    print ("Folder created")
except OSError as err:
    if err.errno == 17:
        print("Dir already exist moving on")
print("To check if python moved on")
