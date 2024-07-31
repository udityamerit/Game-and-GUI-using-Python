from tkinter import *
from PIL import ImageTk, Image 

      
root  = Tk()

# img= PhotoImage(file='image.png', master= root)
# img_label= Label(root,image=img)
# img_label.place(x=0, y=0)
 
root.configure(background='lightblue')
def getvalue():
        print("Form submission succesful")

        print(f" Name: {namevalue.get()}\n Phone Number:  {Phonevalue.get()}\n Gender: {gendervalue.get()}\n Emergency Contact Number: {emergencyvalue.get()}\n Payment method: {paymentvalue.get()}\n\n")

        with open('7.1_record.text','a') as f:
                f.write(f" Name: {namevalue.get()}\n Phone Number:  {Phonevalue.get()}\n Gender: {gendervalue.get()}\n Emergency Contact Number: {emergencyvalue.get()}\n Payment method: {paymentvalue.get()}\n\n")


root.title("My first form")

icon = PhotoImage(file="books.png")
root.iconphoto(True,icon)

root.geometry("700x400")

# heading creating
Label(root, text="Welcome to home", font="robotomono,15,bold",background="orange",relief="raised",borderwidth=5).grid(row=0, column=3,pady=3)

# creating the labels
name = Label(root,text="Name" ,font="robotomono,10,bold",bg='lightblue')
Phone = Label(root, text="Phone",font="robotomono,10,bold",bg='lightblue')
gender = Label(root, text="Gender",font="robotomono,10,bold",bg='lightblue')
emergency  = Label(root, text="Emergency Contact",font="robotomono,10,bold",bg='lightblue')
payment = Label(root, text="Payment Mode",font="robotomono,10,bold",bg='lightblue')

# packing of all the labels
name.grid(row=1, column = 2)
Phone.grid(row=2, column = 2)
gender.grid(row=3, column = 2)
emergency.grid(row=4, column = 2)
payment.grid(row=5, column = 2)

# creating variables to take the inputs and checkboxes
namevalue = StringVar()  # this is use for the taking input
Phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()   # this is use for the checkbox

# creating the entry variables so that we can take the input
nameentry = Entry(root, textvariable=namevalue,font="robotomono,10,bold",fg='blue')
Phoneentry = Entry(root, textvariable= Phonevalue,font="robotomono,10,bold")
genderentry = Entry(root, textvariable=gendervalue ,font="robotomono,10,bold")
emergencyentry = Entry(root, textvariable=emergencyvalue ,font="robotomono,10,bold")
paymententry = Entry(root, textvariable=paymentvalue ,font="robotomono,10,bold")

# packing all the elements of the entries
nameentry.grid(row=1, column=3,pady=5)
Phoneentry.grid(row=2, column=3,pady=5)
genderentry.grid(row=3, column=3,pady=5)
emergencyentry.grid(row=4, column=3,pady=5)
paymententry.grid(row=5, column=3,pady=5)

# checkbox and packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable= foodservicevalue,font="robotomono,10,bold",bg='lightblue')
foodservice.grid(row=6, column=3, pady=5)

# Button & packing it
Button(text="Sumbmit the form", command=getvalue,background="gold",relief="sunken",borderwidth=5,font="robotomono,8,bold",fg="green").grid(row=7,column=3,pady=5)

root.mainloop()