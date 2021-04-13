# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/4/13 19:12
software: PyCharm

Description:
    we can set button font and width as well as function
"""
import tkinter

window = tkinter.Tk()
window.title('mywindow')
window.geometry('200x200')


def plus():
    n1 = e1.get()  # 获取输入框1的值
    n2 = e2.get()  # 获取输入框2的值
    t.delete(1.0, 'end')  # 清除文本框内容
    t.insert('insert', int(n1) + int(n2))  # 将结果添加到文本框显示


l1 = tkinter.Label(window, text='输入数字1')
l1.pack()
# 定义输入框1
e1 = tkinter.Entry(window, width=15)
e1.pack()
# 定义输入框2
l2 = tkinter.Label(window, text='输入数字2')
l2.pack()
e2 = tkinter.Entry(window, width=15)
e2.pack()

b1 = tkinter.Button(window, text="计算两数之和", command=plus)
b1.pack()
# 定义文本框
t = tkinter.Text(window,
                 state='normal',  # 有disabled、normal两个状态值，默认为normal
                 width=15, height=2
                 )
t.pack()
b2 = tkinter.Button(window, text='退出', command=window.quit)
b2.pack()

window.mainloop()
