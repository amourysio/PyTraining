from tkinter import *
from tkinter import filedialog


def openFile():
    # filePath = filedialog.askopenfilename(initialdir="C:\\Users\\hoamo\\Desktop\\PythonProjects\\pyTraining\\file")
    filePath = filedialog.askopenfilename(title="File Path",filetypes=(("text files","*.txt"),("all files","*,*")))

    file = open(filePath,"r")
    print(file.read())
    file.close()


window = Tk()

button = Button(text="Open",command=openFile)
button.pack()

window.mainloop()