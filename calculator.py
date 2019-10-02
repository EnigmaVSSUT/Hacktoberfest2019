from tkinter import *
w=Tk()

eq=StringVar()
expr=""
def buttonclk(n):
    global expr
    expr=expr+str(n)
    eq.set(expr)
    
def calculate():
    global expr
    res=eval(expr)
    eq.set(res)

def clear():
    global expr
    expr=""
    eq.set(expr)

w.geometry("517x300")
w.title("Simple Calculator")
e1=Entry(w,font=("arial",20,"bold"),textvariable=eq,justify="right")
b1=Button(w,text="1",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(1))
b2=Button(w,text="2",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(2))
b3=Button(w,text="3",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(3))
b4=Button(w,text="4",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(4))
b5=Button(w,text="5",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(5))
b6=Button(w,text="6",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(6))
b7=Button(w,text="7",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(7))
b8=Button(w,text="8",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(8))
b9=Button(w,text="9",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(9))
b10=Button(w,text="0",font=("arial",20,"bold"),width=7,command=lambda:buttonclk(0))
b11=Button(w,text="=",font=("arial",20,"bold"),width=7,command=calculate)
b12=Button(w,text="clc",font=("arial",20,"bold"),width=7,command=clear)
b13=Button(w,text="+",font=("arial",20,"bold"),width=7,command=lambda:buttonclk("+"))
b14=Button(w,text="-",font=("arial",20,"bold"),width=7,command=lambda:buttonclk("-"))
b15=Button(w,text="*",font=("arial",20,"bold"),width=7,command=lambda:buttonclk("*"))
b16=Button(w,text="/",font=("arial",20,"bold"),width=7,command=lambda:buttonclk("/"))

e1.grid(columnspan=5,ipadx=100)
b1.grid(row=2, column=1)
b2.grid(row=2, column=2)
b3.grid(row=2, column=3)
b4.grid(row=2, column=4)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=3, column=3)
b8.grid(row=3, column=4)
b9.grid(row=4, column=1)
b10.grid(row=4, column=2)
b11.grid(row=4, column=3)
b12.grid(row=4, column=4)
b13.grid(row=5, column=1)
b14.grid(row=5, column=2)
b15.grid(row=5, column=3)
b16.grid(row=5, column=4)

w.mainloop()
