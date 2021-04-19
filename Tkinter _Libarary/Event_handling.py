# Tutorial 6 Event Handling
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Define Function
def show1(e):
    root.configure(background='pink')

def show2(e):
    root.configure(background='green')

def show3(e):
    root.configure(background='blue')

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2)

# Bind Method used to Bind Mouse keys for Diffrent function
btn.bind("<Button-1>",show1) # Button-1 = Left Mouse Key
btn.bind("<Button-2>",show2) # Button-2 = Mouse Wheel Key
btn.bind("<Button-3>",show3) # Button-3 = Right Mouse Key
btn.pack()

root.mainloop()