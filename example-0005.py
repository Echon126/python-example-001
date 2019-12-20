import sure
import re

(4).should.be.equal(2 + 2)
ret = re.findall('a', 'eva egon yuan')

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re  # 正则表达式
import requests


def butonck():
    # 改变lab颜色
    labelx["fg"] = "green"
    # 获取输入框值
    textx = entryx.get()
    # 去掉字符串前后空格
    textx = textx.strip()
    if textx == '':
        # 弹出提示框
        messagebox.showinfo("东东提示", "输入不可为空")
    else:
        # 字典数据
        datax = {
            "word": textx,
            "sizes": 60,
            "fonts": "lfc.ttf",
            "fontcolor": "#000000"
        }
        rx = requests.post("http://www.uustv.com/", data=datax)
        rx.encoding = "utf-8"
        htmlx = rx.text  # 网站源码
        zz = '<div class="tu">.*?<img src="(.*?)"/></div>'  # 括号里的.*?表示要取的值
        # 取图片地址
        imagex = re.findall(zz, htmlx)
        # 取图片数据
        imagedatax = requests.get("http://www.uustv.com/" + imagex[0]).content
        # 打开文件
        ff = open('{}.gif'.format(textx), "wb")
        # 写图片数据
        ff.write(imagedatax)
        #
        bmx = ImageTk.PhotoImage(file='{}.gif'.format(textx))
        lab2 = Label(rview, image=bmx)
        lab2.bm = bmx
        lab2.grid(row=2, columnspan=2)


# 创建窗口
rview = Tk()
# 标题
rview.title("东小东标题党")
# 窗口大小 长高用小写x隔开
# rview.geometry("600x300")
# 窗口基于屏幕的坐标 +x轴+y轴
rview.geometry("+500+200")
# 创建lab标签
labelx = Label(rview, text="签名", fg="red", font=("宋体", 30))
# 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
labelx.grid(row=0, column=0)
# 创建输入框
entryx = Entry(rview, font=("宋体", 20))
# 显示输入框
entryx.grid(row=0, column=1)
# 创建按钮
buttonx = Button(rview, text="确定", font=("宋体", 30), command=butonck)
# 显示按钮
buttonx.grid(row=1, column=2)
# 显示后改变按钮属性
# buttonx["width"]=2


# 消息循环 显示窗口
rview.mainloop()
