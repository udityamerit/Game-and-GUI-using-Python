from tkinter import *

root = Tk()

root.geometry("700x500")
root.minsize(700,700)
root.maxsize(1000,900)

# creating a frame
f1 = Frame(root,borderwidth=10,bg="gray",relief=SUNKEN)
f1.pack(pady= 10)

f2 = Frame(root,borderwidth=10,bg="orange",relief=SUNKEN)
f2.pack(pady= 10,anchor="nw")

f3 = Frame(root,borderwidth=10,bg="pink",relief=SUNKEN)
f3.pack(pady= 10,anchor="ne")

f4 = Frame(root,borderwidth=10,bg="Yellow",relief=SUNKEN)
f4.pack(pady= 10)

# creating a button 
b1 = Button(f1,fg="red",text="print",font="Robotomon,10,bold")
b1.pack(side=LEFT,padx=20)

b2 = Button(f2,fg="red",text="print",font="Robotomon,10,bold")
b2.pack(side=LEFT,padx=20)

b3 = Button(f3,fg="red",text="print",font="Robotomon,10,bold")
b3.pack(side=LEFT,padx=20)

b4 = Button(f4,fg="red",text="print",font="Robotomon,10,bold")
b4.pack(side=LEFT,padx=20)




root.mainloop()