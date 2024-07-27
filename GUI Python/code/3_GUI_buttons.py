from tkinter import *
# button = you click it, then it does stuff

count = 0

# creating a func() so that i can count the click 
def click():
        global count # using globle keyword to globlise the count variable 
        count +=1 
        print(count)
window = Tk()

Photo = PhotoImage(file="like.png")

window.geometry("450x450")

button = Button(window, text="Click me!",
                command= click, # this is the function name
                font=("Comic Sans",30), # this is font of the text 
                fg= "green",
                background="black",
                state=ACTIVE, # state use to enable or desable the button
                image=Photo, 
                compound="bottom") 

button.pack()

window.mainloop()