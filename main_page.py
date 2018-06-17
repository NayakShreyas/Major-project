import tkinter as tk
from tkinter import *
import twitter_search

class main_page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #Creating the labels
        self.Label_WelMsg=Label(self,text="Data Analytics",font=("Helvetica", 26),bg="red")
        twitter_button = tk.Button(self, text="Go to Twitter Analytics", command=lambda: controller.show_frame("twitter_search"))
        facebook_button = tk.Button(self, text="Go to Facebook Analytics", command=lambda: controller.show_frame("twitter_search"))
        self.Label_WelMsg.pack(fill=X)
        twitter_button.pack()
        facebook_button.pack()

