import tkinter as tk

      
root  = tk.Tk()

root.configure(background='lightblue')

# Difine the function for getting the form details and store the details in file
def getvalue():
        print("Form submission succesful")

        print(f" Name: {namevalue.get()}\n Phone Number:  {Phonevalue.get()}\n Gender: {gendervalue.get()}\n Branch Name : {BranchNamevalue.get()}\n RegestrationNo : {RegestrationNovalue.get()}\n\n")

        # creating a file to store the records
        with open('7.1_record.text','a') as f:
                f.write(f" Name: {namevalue.get()}\n Phone Number:  {Phonevalue.get()}\n Gender: {gendervalue.get()}\n Branch Name : {BranchNamevalue.get()}\n RegestrationNo : {RegestrationNovalue.get()}\n\n")

# settin the title of the window
root.title("Student Submission form")

def exitt():
        root.destroy()

# setting the Size of the window
root.geometry("700x400")

# heading creating
tk.Label(root, text="Welcome to the Contest", font="robotomono,15,bold",background="orange",relief="raised",borderwidth=5).grid(row=0, column=3,pady=3)

# creating the tk.Labels
name = tk.Label(root,text="Name" ,font="robotomono,10,bold",bg='lightblue')
Phone = tk.Label(root, text="Phone",font="robotomono,10,bold",bg='lightblue')
email = tk.Label(root,text="Email Id", font="robotomono,10,bold",bg="lightblue")
gender = tk.Label(root, text="Gender",font="robotomono,10,bold",bg='lightblue')
BranchName  = tk.Label(root, text="Branch Name ",font="robotomono,10,bold",bg='lightblue')
RegestrationNo = tk.Label(root, text="Regestration No ",font="robotomono,10,bold",bg='lightblue')

# packing of all the tk.Labels
name.grid(row=1, column = 2)
Phone.grid(row=2, column = 2)
email.grid(row=3, column = 2)
gender.grid(row=4, column = 2)
BranchName.grid(row=5, column = 2)
RegestrationNo.grid(row=6, column = 2)

# creating variables to take the inputs and checkboxes
namevalue = tk.StringVar()  # this is use for the taking input
Phonevalue = tk.StringVar()
emailvalue = tk.StringVar()
gendervalue = tk.StringVar()
BranchNamevalue = tk.StringVar()
RegestrationNovalue = tk.StringVar()

# creating the tk.Entry variables so that we can take the input
nameentry = tk.Entry(root, textvariable=namevalue,font="robotomono,10,bold",fg='blue')
Phoneentry = tk.Entry(root, textvariable= Phonevalue,font="robotomono,10,bold")
emailentry = tk.Entry(root, textvariable= emailvalue, font="robotomono,10,bold" )
genderentry = tk.Entry(root, textvariable=gendervalue ,font="robotomono,10,bold")
BranchNameentry = tk.Entry(root, textvariable=BranchNamevalue ,font="robotomono,10,bold")
RegestrationNoentry = tk.Entry(root, textvariable=RegestrationNovalue ,font="robotomono,10,bold")

# packing all the elements of the entries
nameentry.grid(row=1, column=3,pady=5)
Phoneentry.grid(row=2, column=3,pady=5)
emailentry.grid(row=3, column=3,pady=5)
genderentry.grid(row=4, column=3,pady=5)
BranchNameentry.grid(row=5, column=3,pady=5)
RegestrationNoentry.grid(row=6, column=3,pady=5)



# Button & packing it
tk.Button(text="Sumbmit the form", command=getvalue,background="gold",relief="sunken",borderwidth=5,font="robotomono,8,bold",fg="green").grid(row=7,column=3,pady=5)


tk.Button(text="Exit",command=exitt,bg="gold",relief="groove",borderwidth=5,font="robotmono,8,bold",fg="red").grid(row=7, column=4,pady=5)
root.mainloop()