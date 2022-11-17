import os
import shutil
text = "Hello,\nMy first creating of file!"

try:
    with open('source.txt', 'w') as file:
        file.write(text)
except Exception as e:
    print(f"The exception is {e}")
finally:
    file.close()

    
source = "source.txt"
destination = 'file/source.txt'
folder = "file"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(f"{source} was moved")
except FileNotFoundError:                                         
    print(f"{source} was not found")


try:
    os.remove(destination)    # delete a file
    # os.rmdir(folder)      # delete an empty directory
    # shutil.rmtree(folder) # delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(f"{destination} was deleted")