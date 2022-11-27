from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\hoamo\\Desktop\\PythonProjects\\pyTraining\\file",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text FIle","*.txt"),
                                        ("HTML File", ".html"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return 
    # fileText = str(text.get(1.0,END))  # write in text area
    fileText = input("Please Enter Text Here: ")
    file.write(fileText)
    file.close()


window = Tk()

button = Button(text="save", command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()