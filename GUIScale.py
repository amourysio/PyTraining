from tkinter import *


def submit():
    print(f"The temperature is: {str(scale.get())} Degrees C")


window = Tk()

flame = PhotoImage(file="logos/flame.png")
snow = PhotoImage(file="logos/snow.png")

hotLabel = Label(image=flame, width=50, height=100)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,  # orientation of scale
              font=("Consolas",20),
              tickinterval=10,  # adds numeric indicators for value
              showvalue=0,   # hide current value
              resolution=5,   # increment of slider
              troughcolor='aqua',
              fg="red",
              bg="black")
scale.set(((scale['from']-scale['to'])/2) + scale['to'])
scale.pack()

coldLabel = Label(image=snow, width=100, height=100)
coldLabel.pack()

button = Button(window,
                text="submit",
                command=submit)
button.pack()
window.mainloop()