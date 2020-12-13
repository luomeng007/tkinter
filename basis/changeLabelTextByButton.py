# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 12:15
software: PyCharm

Description:
"""

from tkinter import *


# method to create child window widget, like here label, this is a very rare method!
def changeLabel():
    # create a child window of lb2
    # because we do not store Label object into a variable when we create Label 'lb2'
    # but the Label is on the root window, so we could create a child window from the root to save get the created Label
    # 'lb2' by using its name. Then we could use lb2.configure to change the text on it.
    lb2 = root.children['lb2']
    # reconfigure children window, we could not see hello, but after three seconds, update text to world!
    # method 1
    lb2['text'] = 'world!'
    # method 2
    # configure is same as config
    # lb2.configure(text='world!')


root = Tk()
# create a label named 'lb2'
Label(name='lb2', text='hello').pack()
Button(text='press to change', command=changeLabel).pack()

root.mainloop()
