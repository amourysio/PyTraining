from tkinter import *


def create_window():
    # new_window = Toplevel()  # new window "on top" of other windows, linked to a "bottom"window
    new_window = Tk()  # Tk() = new independent window
    old_window.destroy()   # close out of old window


old_window = Tk()

Button(old_window,text="Create new Window",command=create_window).pack()

old_window.mainloop()
# window = Tk()
#
# Button(window,text="Create new Window",command=create_window).pack()
#
# window.mainloop()