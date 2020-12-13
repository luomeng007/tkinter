# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/12/13 12:15
software: PyCharm

Description:
"""
import psutil
import time
from tkinter import *


# the first method to write program
# def make_app():
#     app = Tk()
#     app.geometry('200x100')
#     # 背景颜色填充
#     app.config(bg='#303030')
#     # 以lable形式写入文字
#     Label(text='实时网速监控', font=('Hack', 23, 'bold'), bg='#303030', fg='white').pack()
#     # 然而这里额text是固定好的,不会改变,后面要采取手段使这个变动
#     Label(name='lb2', text='_kb/s', font=('Hack', 20, 'bold'), bg='#303030', fg='white').pack()
#     return app
#
#
# def speed_test():
#     s1 = psutil.net_io_counters(pernic=True)['WLAN']
#     time.sleep(1)
#     s2 = psutil.net_io_counters(pernic=True)['WLAN']
#     result = s2.bytes_recv - s1.bytes_recv
#     # 除法结果保留两位小数
#     return str('%.2f' % (result / 1024)) + 'kb/s'
#
#
# def Gui_update(do):
#     data = do()
#     # app下名字是lb2的子控件
#     lb2 = app.children['lb2']
#     # 配置，替换原来的text
#     lb2.config(text=data)
#     # 每1秒后调用lambda:Gui_update(do)函数
#     app.after(1000, lambda: Gui_update(do))
#
#
# # lambda function is necessary, if we leave out lambda, program wrong.
# app = make_app()
# # 每1秒(1000ms)后调用逗号后面的函数,Gui_update(speed_test)函数
# # 如此调用程序会执行,但是实时网速不会改变
# # app.after(1000, speed_test)
# # 我们需要进行如下调用,将speed_test函数传递给Gui_update函数作为参数
# app.after(1000, lambda: Gui_update(speed_test))
# app.mainloop()


# the second method to write program, we only change Gui_update function a little bit
# def Gui_update():
#     data = speed_test()
#     # app下名字是lb2的子控件
#     lb2 = app.children['lb2']
#     # 配置，替换原来的text
#     lb2.config(text=data)
#     # 每1秒后调用lambda:Gui_update(do)函数
#     app.after(1000, lambda: Gui_update())
#
#
# app = make_app()
# # 如此调用直接无线循环,无法启动mainloop循环体
# # Gui_update()
# # 同上,1s后开始进入函数中,一直循环出不来,程序卡死
# # app.after(1000, Gui_update)
# # 采用lambda函数
# app.after(1000, lambda: Gui_update())
# app.mainloop()

# 结论：两种方法均会存在轻微卡顿
# 简化上述写法，并且将窗口固定，实际中应该学习上述写法，模块化作用分明
def refreshText():
    s1 = psutil.net_io_counters(pernic=True)['WLAN']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['WLAN']
    result = s2.bytes_recv - s1.bytes_recv
    lb2 = windows.children['lb2']
    lb2.config(text=str(result) + 'kb/s')
    windows.after(1000, refreshText)


windows = Tk()
windows.geometry('200x100')
windows.config(bg='#303030')
windows.overrideredirect(True)
Label(text='实时网速监控', font=('Hack', 23, 'bold'), bg='#303030', fg='white').pack()
Label(name='lb2', text='_kb/s', font=('Hack', 20, 'bold'), bg='#303030', fg='white').pack()
windows.after(1000, refreshText)
windows.mainloop()
