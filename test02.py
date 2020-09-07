# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:46:30 2020

@author: 15025

Get the input from entry, and pass parameters to command of button by using lambda function.
"""

import tkinter as tk


class Gui(tk.Tk):
    def __init__(self):
        # create tkinter window object
        super().__init__()
        # set the name of window
        self.title("Debug")
        # set the size of window
        self.geometry("1000x800+400+100")
        self.mainGui()
        
        
    def mainGui(self):
        # create a label
        label = tk.Label(self, text="user name")
        # set the label in a specific position
        label.pack()
        # create an entry
        user_text=tk.Entry()
        # set the entry in a specific position
        user_text.pack()
        
        
        def getTextInEntry(user_text):
            user = user_text.get()
            print(user)

        
        # set a button, when click it, read the content in entry
        button = tk.Button(self,text="login",command=lambda: getTextInEntry(user_text))
        # set the button in a specific position
        button.pack()
        
        # start mainloop
        self.mainloop()


if __name__ == "__main__":
    main = Gui()
