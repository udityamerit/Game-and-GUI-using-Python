from tkinter import *



        
root  = Tk()

def getvalue():
        print("Form submission succesful")

        print(f"{namevalue.get(), Phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get()}")

        with open('7.1_record.text','a') as f:
                f.write(f"{namevalue.get(), Phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get()}\n")


root.title("My first form")
icon = PhotoImage(file="books.png")
root.iconphoto(True,icon)

root.geometry("744x444")

# heading creating
Label(root, text="Welcome to the exercise", font="robotomono,10,bold").grid(row=0, column=3,pady=5)

# creating the labels
name = Label(root,text="Name")
Phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency  = Label(root, text="Emergency Contact")
payment = Label(root, text="Payment Mode")

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
nameentry = Entry(root, textvariable=namevalue)
Phoneentry = Entry(root, textvariable= Phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

# packing all the elements of the entries
nameentry.grid(row=1, column=3)
Phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# checkbox and packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable= foodservicevalue)
foodservice.grid(row=6, column=3, pady=5)

# Button & packing it
Button(text="Sumbmit the form", command=getvalue).grid(row=7,column=3)

root.mainloop()