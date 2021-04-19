# Tutorial 7 Event Handling by Lamda expression
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Define Function

show1=lambda e:root.configure(background='red')
show2=lambda e:root.configure(background='green')
show3=lambda e:root.configure(background='blue')

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2)

# Bind Method used to Bind Mouse keys for Diffrent function
btn.bind("<Button-1>",show1) # Button-1 = Left Mouse Key
btn.bind("<Button-2>",show2) # Button-2 = Mouse Wheel Key
btn.bind("<Button-3>",show3) # Button-3 = Right Mouse Key
# To perform any action on Double click then simply replace <Button-1> to <Double-1>
btn.pack()

root.mainloop()