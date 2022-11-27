from tkinter import *

# button = you click it, then does stuff

count = 0

def click():
    global count
    count += 1
    print(f"You click Button! {count}")


window = Tk()

icon = PhotoImage(file="logos/like.png")

button = Button(window,
                text="Click Me",
                command=click,
                font=("Comic Sans",30),
                fg="green",
                bg="black",
                activebackground="green",
                activeforeground="black",
                state=ACTIVE,
                image=icon,
                compound="top")

button.pack()

window.mainloop()