# Tutorial 9 Keyboard Keys Fuctioning
from tkinter import *

root=Tk()
root.minsize(600,300)
root.resizable(0,0)

# Define Function

show1=lambda e:root.configure(background='red')
show2=lambda e:root.configure(background='blue')
show3=lambda e:root.configure(background='green')
show4=lambda e:root.configure(background='white')
show5=lambda e:root.configure(background='black')
show6=lambda e:root.configure(background='pink')

# Keyboard keys funtioning
root.bind("<r>",show1) 
root.bind("<b>",show2) 
root.bind("1",show3)
root.bind("<Shift-Up>",show4)
root.bind("<Alt-Down>",show5)
root.bind("<Control-Left>",show6)   
# To define number Keys then put "1" inplace "<1>" 

root.mainloop()