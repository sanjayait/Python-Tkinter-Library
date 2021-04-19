# Tutorial 13 Mathematical Operations by defferent Functions
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

def add():
    a=x.get()
    b=y.get()
    sum=a+b
    print(sum)
    z.set(sum)
    x.set("")
    y.set("")

def sub():
    a=x.get()
    b=y.get()
    sub=a-b
    print(sub)
    z.set(sub)
    x.set(""),y.set("")

# String Variable Class
x=DoubleVar() # You can Set IntegerVar for numerical value
y=DoubleVar()
z=DoubleVar()

# Create Input field
e1=Entry(root,font=("Arial",15),textvariable=x)
e1.pack(pady=25)

# Create Input field
e2=Entry(root,font=("Arial",15),textvariable=y)
e2.pack(pady=25)


# Create Button
btn=Button(root,text='+',bg='lightblue',fg='black',width=10,height=2,command=add)
btn.pack()
btn=Button(root,text='-',bg='lightblue',fg='black',width=10,height=2,command=sub)
btn.pack()

# Create Input field
e3=Entry(root,font=("Arial",15),textvariable=z)
e3.pack(pady=25)


root.mainloop()