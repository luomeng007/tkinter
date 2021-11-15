# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/4/13 19:12
software: PyCharm

Description:
    we can set label font and width as well as background
"""
import tkinter

window = tkinter.Tk()
window.title('my window')
window.geometry('200x180')

l = tkinter.Label(window,
                  text='This is Label!',  # 标签的文字
                  bg='pink',  # 背景颜色
                  font=('Arial', 12),  # 字体和字体大小
                  width=15, height=2,  # 标签长宽
                  ) # 创建label时关键字text=不能省略
# 固定窗口位置
l.pack()

window.mainloop()
