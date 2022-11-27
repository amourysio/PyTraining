from tkinter import *

# entry widget = textbox that accept a single line of user input


def submit():
    username = entry.get()
    print(f"Hello {username}")
    entry.config(state=DISABLED)


def delete():
    entry.delete(0,END)


def backspace():
    entry.delete(len(entry.get())-1,END)


window = Tk()

entry = Entry(window,
              font=("Arial",50),
              fg="green",
              bg="black",
              show="*")

entry.insert(0,"password")
entry.pack(side=LEFT)

submitButton = Button(window,text="submit", command=submit)
submitButton.pack(side=RIGHT)

deleteButton = Button(window,text="delete", command=delete)
deleteButton.pack(side=RIGHT)

backspaceButton = Button(window,text="<--", command=backspace)
backspaceButton.pack(side=RIGHT)

window.mainloop()