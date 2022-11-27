from tkinter import *


def display():
    if x.get():
        print("You agree!")
    else:
        print("You don't agree :(")


window = Tk()

image1 = PhotoImage(file="logos/py.png")
x = BooleanVar()
checkbutton = Checkbutton(window,
                          text="check button",
                          variable=x,
                          onvalue=True,
                          offvalue=False,
                          command=display,
                          font=("Arial",20),
                          fg="#00FF00",
                          bg="black",
                          activeforeground="green",
                          activebackground="black",
                          pady=10,
                          padx=10,
                          image=image1,
                          compound="left")

checkbutton.pack()
window.mainloop()