# Tutorial 11 String Variable Class
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

def show():
    s=x.get()
    print(s)
    x.set("")

# String Variable Class
x=StringVar()

# Create Input field
e=Entry(root,font=("Arial",15),textvariable=x)
e.pack()

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2,command=show)
btn.pack()

root.mainloop()