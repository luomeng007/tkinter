# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 12:03
software: PyCharm

Description:
"""
from tkinter import *


def hello(event):
    print("Single Click, Button-l")


def quit(event):
    print("Double Click, so let's stop")
    import sys
    sys.exit()


widget = Button(None, text='Mouse Clicks')
widget.pack()
# 将按键与点击事件结合在一起,<Button-1>为左键单击事件,<Double-1>为左键双击事件
# 注意这里双击退出时,会先出发左键单击事件,然后触发双击事件
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()
