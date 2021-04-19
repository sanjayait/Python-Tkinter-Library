# Tutorial 18 How to link one GUItkinter window to another
from tkinter import *

root=Tk()
root.minsize(500,400)
root.resizable(0,0)

# Define function
def login():
    f2=Frame();f2.place(x=0,y=0,width=500,height=400)
    e1=Entry(f2);e1.pack()
    e2=Entry(f2);e2.pack()
    e3=Entry(f2);e3.pack()
    b1=Button(f2,text="Back",command=home);b1.pack()
    b2=Button(f2,text="Login");b2.pack()

def registration():
    f3=Frame();f3.place(x=0,y=0,width=500,height=400)
    e1=Entry(f3);e1.pack()
    e2=Entry(f3);e2.pack()
    b1=Button(f3,text="Back",command=home);b1.pack()
    b2=Button(f3,text="Registar");b2.pack()

def home():
    f1=Frame();f1.place(x=0,y=0,width=500,height=400)
    b1=Button(f1,text="Login page",command=login);b1.pack()
    b2=Button(f1,text="Registration",command=registration);b2.pack()
home()


root.mainloop()