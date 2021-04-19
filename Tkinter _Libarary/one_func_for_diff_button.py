# Tutorial 14 Define one funcion for diffrent buttons
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# String Variable Class
x=DoubleVar() # You can Set IntegerVar for numerical value
y=DoubleVar()
z=DoubleVar()

def show(op):
    a,b=x.get(),y.get()
    if op==1:
        z.set(a+b)
    if op==2:
        z.set(a-b)
    if op==3:
        z.set(a*b)


# Create Input field
e1=Entry(root,font=("Arial",15),textvariable=x)
e1.pack(pady=25)
e2=Entry(root,font=("Arial",15),textvariable=y)
e2.pack(pady=25)


# Create Button
btn=Button(root,text='+',bg='lightblue',fg='black',width=10,height=2,command=lambda:show(1))
btn.pack()
btn=Button(root,text='-',bg='lightblue',fg='black',width=10,height=2,command=lambda:show(2))
btn.pack()
btn=Button(root,text='x',bg='lightblue',fg='black',width=10,height=2,command=lambda:show(3))
btn.pack()

# Create Input field
e3=Entry(root,font=("Arial",15),textvariable=z)
e3.pack(pady=25)

root.mainloop()