#--*--coding:utf-8--*--
from  Tkinter import *
import subprocess
from time import strftime,gmtime
from datetime import datetime
import tkMessageBox,os
class T:
    def __init__(self,t):#对输入的时间进行切片分割取出各项时间值
        self.h=int(t[:2])  #小时
        self.m=int(t[3:5])  #分钟
        self.s=int(t[6:9])   #秒
        self.n=int(t[9:13])   #年
        self.y=int(t[14:16])   #月
        self.r=int(t[17:19])    #日

class app(Frame):
    def __init__(self,master=None):  #主框架初始化
        Frame.__init__(self,master)
        self.pack()
        self.CreatWidgets()
    def CreatWidgets(self):
        self.h=Entry(self)
        self.h.pack()
        self.h.insert(0,datetime.now().strftime('%H:%M:%S %Y-%m-%d'))  #插入当前的时间值，便于用户设置时间
        self.b=Button(self,text="确定关机",command=self.shutdown)
        self.b.pack()
    def shutdown(self):  #点击button事件的处理函数
        t=self.h.get()
        st=T(str(t))
        flag=0
        stime=datetime(st.n,st.y,st.r,st.h,st.m,st.s)
        j=(stime-datetime.now()).total_seconds()+1
        if j<0:
            tkMessageBox.showinfo("警告","不能设置成小于当前时间！")
            return 0
        else:
            while flag==0:
                try:
                    v = subprocess.check_output('shutdown -s -t %d'%j,shell=True) #shell=True表示接受字符串变量，如果False则是接受列表变量
                    flag=1
                except:
                    flag=0
                    subprocess.check_output('shutdown -a',shell=True)
        tkMessageBox.showinfo("message","设置成功！")

a=app()
a.master.title("定时关机小程序")
a.master.geometry('250x150')
a.mainloop()