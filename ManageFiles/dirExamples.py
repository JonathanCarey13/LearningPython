import os
# Creates a list of the files in the current directory
os.listdir(os.getcwd())
# Creates variable for directory I want to check, in this case we'll use the current directory
dir = os.getcwd()
# Iterates through the file names returned by the variable dir
for name in os.listdir(dir):
    # Creates a string by joining the directory of each file with the file's name
    fullname = os.path.join(dir, name)
    # Use that fullname and the isdir() method to see if its a directory
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))