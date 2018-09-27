# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/9/3 20:29
'''

from tkinter import *

top = Tk()
top.title('wojiaomaweichang')
top.geometry('400x400')
top.resizable(width=True,height=True)

li = ['c','python','php','html','sql','java']
movie = ['CSS','JQuery','Bootstrap']

l = Label(top,text='maweichang',bg='green',font=('Arial',12),width=10,height=2)


listb = Listbox(top,width=20,height=6)
listb2 = Listbox(top)

for item in li:
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)
l.pack()
listb.pack()
listb2.pack()
top.mainloop()