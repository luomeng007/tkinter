# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:56:28 2020

@author: 15025

delete image widget of tkinter
"""

import os
import tkinter as tk
from PIL import Image
from PIL import ImageTk


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
        if os.path.exists(r"C:/Users/15025/Desktop/IPHT/figureSliceInInterval/1.png"):
            image = Image.open("C:/Users/15025/Desktop/IPHT/figureSliceInInterval/1.png")
            photo = ImageTk.PhotoImage(image)
            self.label1 = tk.Label(self.tk, image=photo)
            self.label1.image = photo
            self.label1.grid()
        
        tk.Button(self.tk, text="delete label", command=self.delete).place(x=100,y=600)
        
    def delete(self):
        self.label1.grid_forget()
        

if __name__ == '__main__':
    main = DeleteWidget()
    main.mainProgram()