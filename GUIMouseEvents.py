from tkinter import *


def doSomthing(event):
    print(f"Mouse coordinates: {str(event.x)} {str(event.y)}")


window = Tk()

# window.bind("<Button-1>",doSomthing)
# window.bind("<Button-2>",doSomthing)
# window.bind("<Button-3>",doSomthing)
# window.bind("<Button-4>",doSomthing)
# window.bind("<ButtonRelease>",doSomthing)
# window.bind("<Enter>",doSomthing)
# window.bind("<Leave>",doSomthing)
window.bind("<Motion>",doSomthing)
window.mainloop()