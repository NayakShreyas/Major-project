#import tkinter
import tkinter as tk
from tkinter import *

class login_Frame(Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Creating all the Labels
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        #Creating all the Entries
        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        # Placing all of the labels
        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)

        # placing all of the entries
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        # creating and placing buttons for signup and cancel
        self.button_login = Button(self, text="Sign Up")
        self.button_cancel = Button(self, text="Cancel")
        self.button_login.grid(row=2)
        self.button_cancel.grid(row=2, column=2)
        self.pack()

        #Define functions for login and cancel button