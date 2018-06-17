#import tkinter
from tkinter import *

class SignUp_Frame(Frame):
    def __init__(self,master):
        super(SignUp_Frame, self).__init__(master)

        #Heading of the Page
        self.label_heading=Label(self,text="Enter the Details")

        #Creating all the Labels
        self.label_username=Label(self,text="Username")
        self.label_password=Label(self,text="Password")
        self.label_vendorId=Label(self,text="Vendor ID")
        self.label_vendorName=Label(self,text="Vendor Name")
        self.label_email=Label(self,text="Email Id")

        #Creating all the Entries
        self.entry_username=Entry(self)
        self.entry_password=Entry(self,show="*")
        self.entry_vendorId=Entry(self)
        self.entry_vendorName=Entry(self)
        self.entry_email=Entry(self)

        #Placing all of the labels
        self.label_heading.grid(row=0,columnspan=2)
        self.label_username.grid(row=1,sticky=E)
        self.label_password.grid(row=2,sticky=E)
        self.label_vendorId.grid(row=3,sticky=E)
        self.label_vendorName.grid(row=4,sticky=E)
        self.label_email.grid(row=5,sticky=E)

        #placing all of the entries
        self.entry_username.grid(row=1,column=1)
        self.entry_password.grid(row=2,column=1)
        self.entry_vendorId.grid(row=3,column=1)
        self.entry_vendorName.grid(row=4,column=1)
        self.entry_email.grid(row=5,column=1)

        #creating and placing buttons for signup and cancel
        self.button_signUp=Button(self,text="Sign Up")
        self.button_cancel=Button(self,text="Cancel")
        self.button_signUp.grid(row=6)
        self.button_cancel.grid(row=6,column=2)
        self.pack()

#Create the functions for signup and cancel button

root=Tk()
root.title("Sign Up")
sf=SignUp_Frame(root)
root.mainloop()

