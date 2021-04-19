# Tutorial 16 Change label of Button
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Define function to change label of button
def show(b):
    b["text"]="Sold out"
    # You can also change attributes of btn object
    b["bg"]="black"
    b["fg"]="white"
    b["width"]=20

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2,command=lambda:show(btn))
btn.pack()

root.mainloop()