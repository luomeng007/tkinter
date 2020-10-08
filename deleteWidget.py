# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:56:28 2020

@author: 15025

delete lable widget of tkinter
"""

import tkinter as tk


class DeleteWidget:
    def __init__(self):
        self.tk = None
        
        self.label1 = None
        
    
    def mainProgram(self):
        
        self.tk = tk.Tk()
        
        self.tk.title("delete widget")
        
        self.tk.geometry("1100x700+350+150")
        
        self.add()
        
        self.tk.mainloop()
        
        self.delete()
        
    
    def add(self):
        self.label1 = tk.Label(self.tk, text="Set Parameters:")
        self.label1.place(x=100, y=100)
        
        tk.Button(self.tk, text="delete label", command=self.delete).place(x=100,y=600)
        
    def delete(self):
        self.label1.place_forget()
        

if __name__ == '__main__':
    main = DeleteWidget()
    main.mainProgram()
