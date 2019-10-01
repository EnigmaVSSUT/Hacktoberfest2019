from tkinter import *
w=Tk()
#define the function
def generate():
    from random import sample #sample generate multiple random number
    n=sample(range(10),6)
    L1.configure(text=n[0])
    L2.configure(text=n[1])
    L3.configure(text=n[2])
    L4.configure(text=n[3])
    L5.configure(text=n[4])
    L6.configure(text=n[5])
def reset():
    L1.configure(text="...")
    L2.configure(text="...")
    L3.configure(text="...")
    L4.configure(text="...")
    L5.configure(text="...")
    L6.configure(text="...")
    

##Design all components
img=PhotoImage(file="./lotte.gif")
lblimg=Label(w,image=img)
L1=Label(w,text="....",width=2,font=("arial",20,"bold"),\
         relief="solid")
L2=Label(w,text="....",width=2,font=("arial",20,"bold"),\
         relief="solid")
L3=Label(w,text="....",width=2,font=("arial",20,"bold"),\
         relief="solid")
L4=Label(w,text="....",width=2,font=("arial",20,"bold"),\
         relief="solid")
L5=Label(w,text="....",width=2,font=("arial",20,"bold"),\
         relief="solid")
L6=Label(w,text="....",width=2,font=("arial",20,"bold"),\
         relief="solid")
B1=Button(w,text="Get ur lucky no" ,command=generate, font=("arial",20,"bold"))
B2=Button(w,text="Reset" , command=reset,font=("arial",20,"bold"))
###################################################
#####Place the components at proper position ######
###################################################
lblimg.grid(row=1,column=1,rowspan=2)
L1.grid(row=1,column=2)
L2.grid(row=1,column=3)
L3.grid(row=1,column=4)
L4.grid(row=1,column=5)
L5.grid(row=1,column=6)
L6.grid(row=1,column=7)
B1.grid(row=2,column=2,columnspan=4)
B2.grid(row=2,column=6,columnspan=2)















#w.mainloop()
