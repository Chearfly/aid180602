from tkinter import *
from tkinter import ttk 
# from PIL import Image
#建立模块对像
root  = Tk()

#设置窗口标题
root.title("人工智能项目")

#设置显示窗口的大小
root.geometry("700x500")

#设置窗口的宽度是不可变化的，但是他的长度是可变的
root.resizable(width = "true",height = "True")

# l = ttk.Label(root, text="欢迎来到人工智能的项目", bg = "blue", font= ("Arial",15), width=30,\
#  height=5)
# l.grid(side = TOP)#设置项目的名称

# label=Label(root,text='Hello,GUI') #生成标签
# label.pack()        #将标签添加到主窗口
# button1=Button(root,text='聊天',width=8,height = 2) #生成button1
# button1.pack(side=LEFT)         #将button1添加到root主窗口
button2=ttk.Button(root,text='天气').grid(column=3, row=1, sticky=W)#列,行,
# button2.pack(side=LEFT)

# def my_out():
#     root.quit

# button2=ttk.Button(root,text='退出',command = root.quit ,width = 8,height =2)
# button2.grid(side=BOTTOM)

root.mainloop()

