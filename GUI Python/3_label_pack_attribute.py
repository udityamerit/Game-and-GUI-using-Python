from tkinter import *

root = Tk()
root.geometry("455x455")
root.title("My gui")

# Important Label Options
'''
text - adds the text
bd - background
fg - foreground
font - sets the font
padx - x  padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE'''
lable = Label(root,
              text="Hello master", 

              font=("Robotomono",40,"bold"), # this take(font_name, fond size, text type)

        #       other wise

                # font="Robotomono,40,bold", # this take(font_name, fond size, text type)

                fg="Green", # this is used to change the color of the text 

                background="orange", # this is used to change the texts background

                relief=RAISED, # this is use for the type of border of given text

                bd=10, # size of the border

                padx=10, # it is use to shift the text inside the label  in x direction

                pady= 10, # it is use to shift the text inside the label  in y direction
                )  
# Important Label Options
'''
anchor = nw,sw,se means(ne = north east, sw = south west)
side = top, bottom, left, right
fill - as window move the box is fill in sliding the window
padx
pady
500x400
'''


lable.pack(side=BOTTOM, anchor="sw", fill=X,)

root.mainloop()