from tkinter import *

# label = an area widget that hold text and/or an image within a window

window = Tk()
photo = PhotoImage(file="logos\\logo.png")

txt = "Hello World"
fontT = ("Arial", 40,"bold")
fg = "green"  # or Hex Value
bg = "black"
label = Label(window,
              text=txt,
              font=fontT,
              fg=fg,
              bg=bg,
              relief=RAISED,
              bd=100,
              padx=20,
              pady=20,
              image=photo,
              compound="top")
window.iconphoto(True,photo)
window.title("GUI Label")
# label.place(x=0,y=100)

label.pack()
window.geometry("500x500")

window.mainloop()