# Tutorial 10 Submit Button
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

def show():
    s=e.get()
    print(s)

# Create Input field
e=Entry(root,font=("Arial",15))
e.pack()

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2,command=show)
btn.pack()

root.mainloop()