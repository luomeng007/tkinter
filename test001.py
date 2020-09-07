# -*-coding:utf-8-*-

import tkinter
import tkinter.messagebox


class Gui:
    def mainProgram(self):
        # define a button
        def buttonClick():
            tkinter.messagebox.showinfo("Hallo, welcome to my World!")
        
        # 创建窗体
        window = tkinter.Tk()
        
        # creat a interface 400*300 resolution, width:400,height:300,the horizontal position 400, the vertical position 200
        window.geometry("400x300+400+200")
        
        window.title("The world of Inkfish")
        # first parameter: window, second: display word
        # creat a label
        label = tkinter.Label(window, text="Programming change the world!")
        # pacl the label we created before
        label.pack()
        
        # creat a button, text "Surprise" is red and the background is blue
        btn = tkinter.Button(window, text="Surprise",command=buttonClick, fg="red", bg="blue")
        btn.pack()
        
        # strat mainloop
        tkinter.mainloop()
        

main = Gui()
main.mainProgram()
