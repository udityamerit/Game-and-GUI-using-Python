from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("455x244")
# for png photos only

photo = PhotoImage(file="rubberwhale1.png")
lb = Label(image=photo)
lb.pack()

# for jpg photo
image = Image.open("aloeL.jpg")
photo = ImageTk.PhotoImage(image)
lb = Label(image=photo)
lb.pack()
root.mainloop()