import os

path = "C:\Users\hoamo\Desktop\PythonProjects\Lectures\pythonProject\test.txt"

if os.path.exist(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")
    