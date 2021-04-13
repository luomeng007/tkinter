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
window.title('my window')
window.geometry('200x180')

l = tkinter.Button(window,
                   text='退出',  # 按钮的文字
                   bg='pink',  # 背景颜色
                   width=15, height=2,  # 按钮长宽
                   command=window.quit
                   )
# 固定窗口位置
l.pack()

window.mainloop()
