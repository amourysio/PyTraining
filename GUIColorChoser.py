from tkinter import *
from tkinter import colorchooser


def click():
    window.config(bg=colorchooser.askcolor()[1])
    # color = colorchooser.askcolor()
    # colorHex = color[1]
    # window.config(bg=colorHex)
    # print(color)
    # print(colorHex)


window = Tk()
window.geometry("420x420")
button = Button(text="Color",command=click)
button.pack()

window.mainloop()