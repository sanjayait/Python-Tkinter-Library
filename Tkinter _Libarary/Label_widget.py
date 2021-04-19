# Tutorial 1 Label widget
from tkinter import *

# Create window object
root=Tk()

# Define size of window
root.minsize(600, 300)
# To fix size of window
root.resizable(0, 0)

# Create label in window using "Label" class
lbl=Label(root,text="Sanjay\nGoyal\nBhind",font=("Arial",15),bg='lightgreen',fg='black',width=40,
            height=3)
lbl.pack()


root.mainloop()
