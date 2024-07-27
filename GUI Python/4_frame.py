from tkinter import *

root = Tk()

root.geometry("1000x500")

# creating a frame

f1 = Frame(root,background="skyblue",borderwidth=6,relief=RAISED,padx=0, pady=10)
f1.pack(side=LEFT,fill="y")

l = Label(f1,text="Creating the different frams in side the window",fg="blue",bg="yellow",font="Robotomono,20,bold",pady= 20)
l.pack()

f2 = Frame(root,background="gray",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l = Label(f2,text="Welcome to the GUI world",fg="red",bg="pink",font="Helvetica,20,bold",pady=20)
l.pack()

root.mainloop()