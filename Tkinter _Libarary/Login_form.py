# Tutorial 4 Login form
from tkinter import *

root=Tk()

root.minsize(400,400)
root.resizable(0,0)

# Pack method use to pack widget in middle of window
# Grid method use to define possition of widget

lb1=Label(root,text='Enter Name: ',font=("Arial",12))
lb1.grid(row=0,column=0,pady=25,padx=25,sticky=W)

ent1=Entry(root,font=("Arial",12))
ent1.grid(row=0,column=1)

lb1=Label(root,text='Enter Password: ',font=("Arial",12))
lb1.grid(row=1,column=0,padx=25,sticky=W)

ent1=Entry(root,font=("Arial",12),show="*")
ent1.grid(row=1,column=1)

btn=Button(root,text='Login',font=("Arial",12),bg='skyblue',width=10)
btn.grid(row=2,column=0,columnspan=2,pady=25)
# Columnspan used to merge columns


root.mainloop()