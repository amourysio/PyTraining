#  frame = a rectangular container to group and hold widgets
from tkinter import *

def clickW():
    print("W is Clicked!")

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# frame.pack(side=BOTTOM)
frame.place(x=50,y=50)

Button(frame,text="W",font=("Consolas",20),command=clickW).pack(side=TOP)
Button(frame,text="A",font=("Consolas",20)).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",20)).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",20)).pack(side=LEFT)

window.mainloop()