# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 15:35
software: PyCharm

Description:
    StringVar是创建Tkinter字符串变量的Tkinter构造函数的一种类型。
    将StringVar变量与Tkinter控件关联后，修改StringVar变量后，Tkinter将自动更新此控件。
"""
import tkinter as tk


class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set("Test")
        self.label = tk.Label(self.root, textvariable=self.text)

        self.button = tk.Button(self.root,
                                text="Click to change text below",
                                command=self.changeText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def changeText(self):
        self.text.set("Text updated")


app = Test()
