# Creating a newspaper of photos

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title("NewsPaper of photo")
root.geometry("500x400")
root.minsize(700,700)
root.maxsize(1000,1000)
im1 = PhotoImage("basketball1.png")
lb = Label(image=im1)
lb.pack()

label = Label(root,text="My First Newspaper", fg="blue", bg="yellow",borderwidth=20,font=("Robotomono",40,"bold"),padx=10,pady=10,relief=RAISED,bd=10)

label.pack(padx=20,pady=10,fill=X)

root.mainloop()