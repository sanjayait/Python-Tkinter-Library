# Tutorial 5 Working-Button
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Define a function
def show():
    print('Hello World')

colorlist=['red','green','blue','yellow','black','pink','orange']
def bgcolor1():
    root.configure(background='lightblue')

def bgcolor2():
    root.configure(background='lightgreen')

def bgcolor3():
    root.configure(background='lightyellow')

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2,command=bgcolor1)
btn.grid(row=0,column=0,pady=10,padx=25)

btn=Button(root,text='Click !!',bg='lightgreen',fg='black',width=10,height=2,command=bgcolor2)
btn.grid(row=0,column=1,padx=25)

btn=Button(root,text='Click !!',bg='lightyellow',fg='black',width=10,height=2,command=bgcolor3)
btn.grid(row=0,column=2,padx=25)

root.mainloop()