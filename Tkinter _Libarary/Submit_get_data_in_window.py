# Tutorial 12 Submit and get data in same window
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

def show():
    a=x.get()
    b=y.get()
    a,b=float(a),float(b)
    sum=a+b
    print(sum)
    z.set(sum)
    x.set("")
    y.set("")

# String Variable Class
x=StringVar() # You can Set IntegerVar for numerical value
y=StringVar()
z=StringVar()

# Create Input field
e1=Entry(root,font=("Arial",15),textvariable=x)
e1.pack(pady=25)

# Create Input field
e2=Entry(root,font=("Arial",15),textvariable=y)
e2.pack(pady=25)


# Create Button
btn=Button(root,text='SUM',bg='lightblue',fg='black',width=10,height=2,command=show)
btn.pack()

# Create Input field
e3=Entry(root,font=("Arial",15),textvariable=z)
e3.pack(pady=25)


root.mainloop()