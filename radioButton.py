from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]


def order():
    if x.get() == 0:
        print("You order a pizza!")
    elif x.get() == 1:
        print("You order a hamburger!")
    elif x.get() == 2:
        print("You order a hotdog!")
    else:
        print("huh?")
window = Tk()

pizza_image = PhotoImage(file="logos/pizza.png")
hamburger_image = PhotoImage(file="logos/hamb.png")
hotdog_image = PhotoImage(file="logos/hotdog.png")
foodImage = [pizza_image, hamburger_image, hotdog_image]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radio buttons
                              variable=x,   # groups radio button together if they share the same variable
                              value=index,   # assigns each radio button a different value
                              padx=25,  # adds padding on x-axis
                              font=("Impact",50),
                              image=foodImage[index],  # adds image to radio button
                              compound="left",   # adds image & text (left-side)
                              indicatoron=0,    # eliminate circle indicators
                              width=600,     # sets width of radio button
                              command=order     # set command of radio button to function
                              )
    radiobutton.pack(anchor=W)

window.mainloop()