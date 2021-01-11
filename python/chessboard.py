from tkinter import *
win = Tk()
win.geometry("500x500")
#win.resizable(0,0)
canvas = Canvas(win)
i=0
j=0
heiorbai=False

for i in range(20):
    for j in range(20):
        canvas.create_rectangle(20*j,20*j,20*i,20*i,)
def dianji(x,y):
    global canvas,heiorbai
    if heiorbai:
        heiorbai=False
        canvas.create_oval(x-5,y-5,x+5,y+5,fill="white")
    else:
        heiorbai=True
        canvas.create_oval(x-5,y-5,x+5,y+5,fill="black")
def paint(event):
    ii=1
    jj=1
    print (event.x,event.y)
    for ii in range(1,19):#去除边框部分不需要使用
        if ((event.x) % 10 )>= 5:
            event.x=event.x +10-((event.x) % 10)
        else:
            event.x=event.x -((event.x) % 10)
        if event.x == ii*20:
            for jj in range(1,19):
                if ((event.y) % 10 )>= 5:
                    event.y=event.y +10-((event.y) % 10)
                else:
                    event.y=event.y -((event.y) % 10)
                if event.y == jj*20:
                    dianji(event.x,event.y)
canvas.bind( "<Button-1>", paint)
canvas.pack()
win.mainloop()
