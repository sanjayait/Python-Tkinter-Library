# Tutorial 3 Button widget
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2)
btn.pack()

root.mainloop()