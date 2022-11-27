from tkinter import *


def openFile():
    print("File has been opened!")


def saveFile():
    print("File has been saved")


def cut():
    print("Text has been cut")


def copy():
    print("Text has been copy")


def paste():
    print("Text has been paste")


window = Tk()


# openImage = PhotoImage(file="logos/open.jfif")
# saveImage = PhotoImage(file="logos/save.jfif")
exitImage = PhotoImage(file="logos/exit.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound="left")

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


window.mainloop()