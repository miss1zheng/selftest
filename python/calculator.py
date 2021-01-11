from tkinter import *
win = Tk()
win.geometry("200x195")
#win.resizable(0,0)

spot_en=False
spot_num=1
tmp=0
all_sum =0
v= StringVar()
v.set(all_sum)
t= StringVar()
t.set(tmp)
symbol= StringVar()
symbol.set("")
def num1():
    calculation_result("1")
def num2():
    calculation_result("2")
def num3():
    calculation_result("3")
def num4():
    calculation_result("4")
def num5():
    calculation_result("5")
def num6():
    calculation_result("6")
def num7():
    calculation_result("7")
def num8():
    calculation_result("8")
def num9():
    calculation_result("9")
def num0():
    calculation_result("0")
def numadd():
    calculation_result("+")
def numsub():
    calculation_result("-")
def nummult():
    calculation_result("*")
def numdiv():
    calculation_result("/")
def numspot():
    calculation_result(".")
def numequal():
    calculation_result("=")

def calculation_result(value):
    global all_sum,tmp,v,spot_en,spot_num,symbol
    global equal,addnum,sub,mult,div
    if(value == "0"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*0
        else:
            tmp=tmp*10+0
    elif(value == "1"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*1
        else:
            tmp=tmp*10+1
    elif(value == "2"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*2
        else:
            tmp=tmp*10+2
    elif(value == "3"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*3
        else:
            tmp=tmp*10+3
    elif(value == "3"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*3
        else:
            tmp=tmp*10+3    
    elif(value == "4"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*4
        else:
            tmp=tmp*10+4
    elif(value == "5"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*5
        else:
            tmp=tmp*10+5            
    elif(value == "6"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*6
        else:
            tmp=tmp*10+6
    elif(value == "7"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*7
        else:
            tmp=tmp*10+7
    elif(value == "8"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*8
        else:
            tmp=tmp*10+8
    elif(value == "9"):
        if spot_en == True:
            spot_num *= 0.1
            print ("spot_num is ",spot_num)
            tmp=tmp+spot_num*9
        else:
            tmp=tmp*10+9
    elif(value == "."):
        spot_en=True
    elif(value == "+"):
        s=symbol.get()
        if(s == "+"):
            addnum()
        elif(s == "-"):
            sub()
        elif(s == "*"):
            mult()
        elif(s == "/"):
            div()
        else:
            all_sum=tmp
        tmp=0
        spot_num=1
        spot_en=False
        symbol.set("+")
    elif(value == "-"):
        s=symbol.get()
        if(s == "+"):
            addnum()
        elif(s=="-"):
            sub()
        elif(s == "*"):
            mult()
        elif(s == "/"):
            div()
        else:
            all_sum=tmp
        tmp=0  
        spot_num=1
        spot_en=False
        symbol.set("-")
    elif(value == "*"):
        s=symbol.get()
        if(s == "+"):
            addnum()
        elif(s == "-"):
            sub()
        elif(s == "*"):
            mult()
        elif(s == "/"):
            div()
        else:
            all_sum=tmp
        tmp=0
        spot_num=1   
        spot_en=False
        symbol.set("*")
    elif(value == "/"):
        s=symbol.get()
        if(s == "+"):
            addnum()
        elif(s == "-"):
            sub()
        elif(s == "*"):
            mult()
        elif(s =="/"):
            div()
        else:
            all_sum=tmp
        tmp=0
        spot_num=1
        spot_en=False
        symbol.set("/")
    elif(value == "="):
        s=symbol.get()
        if(s == "+"):
            addnum()
        elif(s == "-"):
            sub()
        elif(s == "*"):
            mult()
        elif(s == "/"):
            div()
        else:
            all_sum=tmp
        equal()
        tmp=0
        spot_num=1
        spot_en=False
        symbol.set("")
    def equal():
        global all_sum,v,t,tmp
        v.set(all_sum)
        t.set(tmp)
    def addnum():
        global all_sum,tmp
        all_sum += tmp
    def sub():
        global all_sum,tmp
        if all_sum == 0:
            all_sum=tmp
        else:
            all_sum -= tmp
    def mult():
        global all_sum,tmp
        if all_sum == 0:
            all_sum=tmp
        else:
            all_sum *= tmp
    def div():
        global all_sum,tmp
        if all_sum == 0:
            all_sum=tmp
        else:
            all_sum /= tmp;

    v.set(all_sum)
    t.set(tmp)

Button(win,text="9",font="楷体",command=num9,width=5).place(x=0,y=0)
Button(win,text="8",font="楷体",command=num8,width=5).place(x=50,y=0)
Button(win,text="7",font="楷体",command=num7,width=5).place(x=100,y=0)
Button(win,text="+",font="楷体",command=numadd,width=5).place(x=150,y=0)
Button(win,text="6",font="楷体",command=num6,width=5).place(x=0,y=28)
Button(win,text="5",font="楷体",command=num5,width=5).place(x=50,y=28)
Button(win,text="4",font="楷体",command=num4,width=5).place(x=100,y=28)
Button(win,text="-",font="楷体",command=numsub,width=5).place(x=150,y=28)
Button(win,text="3",font="楷体",command=num3,width=5).place(x=0,y=56)
Button(win,text="2",font="楷体",command=num2,width=5).place(x=50,y=56)
Button(win,text="1",font="楷体",command=num1,width=5).place(x=100,y=56)
Button(win,text="×",font="楷体",command=nummult,width=5).place(x=150,y=56)
Button(win,text="0",font="楷体",command=num0,width=5).place(x=0,y=84)
Button(win,text=".",font="楷体",command=numspot,width=5).place(x=50,y=84)
Button(win,text="=",font="楷体",command=numequal,width=5).place(x=100,y=84)
Button(win,text="÷",font="楷体",command=numdiv,width=5).place(x=150,y=84)
Label(win,textvariable=t,font="楷体",bg="white",width=24,borderwidth=2,anchor=W,relief="groove").place(x=0,y=112)
Label(win,textvariable=v,font="楷体",bg="white",width=24,height=2,anchor=W,relief="groove").place(x=0,y=150)
win.mainloop()