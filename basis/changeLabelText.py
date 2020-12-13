# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 12:55
software: PyCharm

Description:
"""
from tkinter import *


class MyGUI:
    def __init__(self):
        self.__mainWindow = Tk()
        # self.frame1 = Frame(self.__mainWindow)
        self.labelText = 'Enter amount to deposit'
        self.depositLabel = Label(self.__mainWindow, text=self.labelText)
        self.depositEntry = Entry(self.__mainWindow, width=10)
        # when we press Enter, event arise, change the text on label
        self.depositEntry.bind('<Return>', self.depositCallBack)
        self.depositLabel.pack()
        self.depositEntry.pack()

        mainloop()

    def depositCallBack(self, event):
        # method 1:
        # self.depositLabel['text'] = 'change the value'
        # method 2:
        self.depositLabel.config(text='change the value')
        print(self.labelText)   # Enter amount to deposit: give original text on label


myGUI = MyGUI()
