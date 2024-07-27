from tkinter import *

root = Tk()

# size control
root.geometry("667x456")

#setting the minsize of our window (width,height)
root.minsize(200,200)

#setting the maxsize of our window(width, height)
root.maxsize(720,720)

# creating a label
hello = Label(text="hello! ")
hello.pack()

root.mainloop()