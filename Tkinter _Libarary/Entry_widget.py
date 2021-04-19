# Tutorial 2 Entry widget(Input Field)
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Create Input Field
ent=Entry(root,font=("Arial",15),fg='red',width=15,bg='blue')
ent.pack()

root.mainloop()