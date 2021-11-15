# -*- coding:utf-8 -*-
"""
author: 15025
time: 15.11.2021   08:01:10
software: PyCharm

Description:
    container.columnconfigure(index, weight)：设定tk窗口grid列布局时的命令
        index：列的index值
        weight: 权重，当前列的宽度尺寸值，相对于其他列宽度的大小
    container.rowconfigure(index, weight)：设定tk窗口grid行布局时的命令
        参数用法同container.columnconfigure(index, weight)
"""
import tkinter as tk

root = tk.Tk()
root.geometry("200x100")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=3)
label1 = tk.Button(root, text="你好")  # 创建label时关键字text不能省略
label2 = tk.Button(root, text="您好")
label1.grid(column=0, row=0)
label2.grid(column=1, row=0)
root.mainloop()

