# Tutorial 15 Print Math Table
from tkinter import *

root=Tk()
root.minsize(300, 300)
root.resizable(0,0)

x=IntVar()

# Define funtion to print table
def show():
    a=x.get()
    for i in range(1,11):
        print(a*i)

# Create Input Field
e1=Entry(root,font=("Arial",15),bg="lightblue",textvariable=x)
e1.grid(row=0,column=0,padx=10,pady=25)

# Create Button
btn1=Button(root,text="Print Table",width=15,height=1,command=show)
btn1.grid(row=0, column=1,padx=10)


root.mainloop()