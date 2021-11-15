# -*- coding:utf-8 -*-
"""
author: 15025
time: 15.11.2021   07:33:31
software: PyCharm

Description:
    usage of StringVar
    创建语法：
        string_var = tk.StringVar(container, value, name)
        container: stringvar需要绑定的窗口，如果不设置，则默认为root控件
        value:  初始值，默认为空字符串。
        name:

    textvariable:
        为了能获取Entry组件上输入的信息，这个参数必须设定为StringVar()对象

"""
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):  # App自身为root控件
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("300x80")

        self.name_var = tk.StringVar()

        self.columnconfigure(0, weight=1)  # 设置三个列，每个列的宽度大小一致
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()  # 自定义创建组件函数

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Name:').grid(column=0, row=0, **padding)

        # Entry
        name_entry = ttk.Entry(self, textvariable=self.name_var)
        name_entry.grid(column=1, row=0, **padding)
        name_entry.focus()  # 这里的focus和focus_set是等价的，将焦点放在当前组件上，当前组件为Entry,所以默认开始输入光标位于Entry组件上

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=1, columnspan=3, **padding)  # **padding的用法也要会

    def submit(self):
        self.output_label.config(text=self.name_var.get())  # 当点击button时，实现对第三行label上文字的实时更新


if __name__ == "__main__":
    app = App()
    app.mainloop()
