# lable: an area widget that holds text and or an image within a window

from tkinter import *

Window = Tk()

Window.geometry("540x540")
Window.title("Adding the lables on window screen")

# setting the icon for the window
icon = PhotoImage(file='graf1.png')
Window.iconphoto(True,icon)

# Adding the photo in the window
photo = PhotoImage(file="graf1.png")

# Adding the lables on window
lable = Label(Window,
              text="Hello master", 

              font=("Robotomono",40,"bold"), # this take(font_name, fond size, text type)

                fg="Green", # this is used to change the color of the text 

                background="orange", # this is used to change the texts background

                relief=RAISED, # this is use for the type of border of given text

                bd=10, # size of the border

                padx=10, # it is use to shift the text inside the label  in x direction

                pady= 10, # it is use to shift the text inside the label  in y direction

                image= photo, # adding the image on window

                compound="bottom")  

lable.pack() # it is used to show the text on the window

Window.config(bg="black") # Changing the background of the window

Window.mainloop()