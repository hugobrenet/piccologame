from tkinter import *

def frame(dict):
    frame = Tk()
    label = Label(
        frame,
        text=dict,
    )
    label.pack()
    frame.mainloop()