from tkinter import *
# grid() = geometry manager that organizes widgets in a table-like structure in a parents


window = Tk()

titleLabel = Label(window,text="Enter your info",font=("Arial",25))
titleLabel.grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First Name: ",width=20,bg="red")
firstNameLabel.grid(row=1,column=0)
firstNameEntry = Entry(window)
firstNameEntry.grid(row=1,column=1)

lastNameLabel = Label(window,text="Last Name: ",bg="green")
lastNameLabel.grid(row=2,column=0)
lastNameEntry = Entry(window)
lastNameEntry.grid(row=2,column=1)

emailNameLabel = Label(window,text="Email: ",bg="blue",width=30)
emailNameLabel.grid(row=3,column=0)
emailNameEntry = Entry(window)
emailNameEntry.grid(row=3,column=1)

Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()