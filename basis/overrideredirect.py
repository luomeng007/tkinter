# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 11:30
software: PyCharm

Description:
"""
import tkinter as Tk

root = Tk.Tk()
root.geometry('200x200+100+100')
root.resizable(False, False)
# 我的理解是这里对widget使用这个方法就可以使widget重新改变大小和形状
root.update_idletasks()
# 将窗口变为无法关闭的,如点右上角的叉和使用alt+F4,也就是只能手动设置退出方式
root.overrideredirect(True)
root.mainloop()