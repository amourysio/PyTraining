from tkinter import *

# widgets = GUI elements: button, text boxes, label, images.
# windows = serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("GUI Program")

# convert from png to Tk
icon = PhotoImage(file="logos/logo.png")
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop()  # place window on computer screen. listen for events

