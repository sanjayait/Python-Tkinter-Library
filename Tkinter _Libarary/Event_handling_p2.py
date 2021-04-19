# Tutorial 8 Event Handling part2
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Define Function

show1=lambda e:root.configure(background='red')
show2=lambda e:root.configure(background='white')

# Create Button
btn=Button(root,text='Click !!',bg='lightblue',fg='black',width=10,height=2)

# To give Hover effect on button
btn.bind("<Enter>",show1) # Enter to give hover effect
btn.bind("<Leave>",show2) # Exit effect
# To perform any action on Double click then simply replace <Button-1> to <Double-1>
btn.pack()

root.mainloop()