from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 50
    download = 0
    speed = 2
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB) * 100
        download += speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent)
percentLabel.pack()

taskLabel = Label(window,textvariable=text)
taskLabel.pack()

button = Button(window,text="download",command=start)
button.pack()

window.mainloop()