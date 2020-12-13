# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 12:36
software: PyCharm

Description:
    method to create child window of root window
"""
from tkinter import *

root = Tk()
t1 = Toplevel(root)
Label(t1, text='This is a child of root').pack(padx=10, pady=10)

root.mainloop()
