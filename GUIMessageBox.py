from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="Info Box",message="Some Text Just Be Here!")
    # while(True):
    #     messagebox.showwarning(title="Info Box",message="Some Text Just Be Here!")
    # messagebox.showerror(title="Info Box", message="Some Text Just Be Here!")
    # if messagebox.askokcancel(title="Ask ok Cancel", message="Do you want to do this?"):
    #     print("You did a this")
    # else:
    #     print("You Canceled a This")
    # if messagebox.askretrycancel(title="Ask ok Cancel", message="Do you want to do this?"):
    #     print("You did a this")
    # else:
    #     print("You Canceled a This")
    # if messagebox.askyesno(title="Ask Yes or No", message="Do you like this"):
    #     print("You click Yes")
    # else:
    #     print("You click No")
    # print(messagebox.askquestion(title="Ask Question", message="Do you like this"))
    # answer = messagebox.askquestion(title="Ask Question", message="Do you like this")
    # if answer == "yes":
    #     print("Yes")
    # else:
    #     print("No")
    answer = messagebox.askyesnocancel(title="Yes, No, Cancel",message="Do you like to Code",icon="error")
    if answer:
        print("You click Yes")
    elif answer == False:
        print("You click No")
    else:
        print("You click Cancel")




window = Tk()

button = Button(window,command=click,text="click me")
button.pack()


window.mainloop()