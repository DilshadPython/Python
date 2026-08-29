from tkinter import *

root = Tk()
root.geometry("750x500")

def getvals():
    print("You have agreed and accepted!")


# Heading
Label(root, text="User Account Registration Form", font=("Arial bold", 20)).grid(row=0, column=4)

# Fields name
name = Label(root, text = "Name")
phone = Label(root, text = "Phone")
email = Label(root, text = "Email")
gender = Label(root, text = "Gender")
paymentmood = Label(root, text = "Payment Mood")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
email.grid(row=3, column=2)
gender.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Variable for Storing Data
namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
gendervalue = StringVar()
paymentmoodvalue = StringVar()

checkvalue = IntVar()

# Creating entry Field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
emailentry = Entry(root, textvariable=emailvalue)
genderentry = Entry(root, textvariable=gendervalue)
paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)

# Packing entry Field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

# Creating checkbox
checkbtn = Checkbutton(root, text="Accept registration?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

# Submit button
Button(text='Submit', command=getvals).grid(row=7, column=3)



root.mainloop()

