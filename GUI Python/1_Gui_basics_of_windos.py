from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

# initialise the window
window = Tk()  

# getting the size of the window
window.geometry("720x540")

# Setting the title of the window name
window.title("My first GUI Program")

# setting the icon for the window
icon = PhotoImage(file='download.png')
window.iconphoto(True,icon)

# changing the background color of the window 
window.config(background="black")

# display the window 
window.mainloop()
