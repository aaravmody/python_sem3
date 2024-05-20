import tkinter
from tkinter import *

root=Tk()
root.title("calci")
root.geometry("300x400")
expression=''

def show():
    global expression
    expression+=value
    result.config(text=expression)

result=Label(root,width=25,height=2,text="",font=("arial",30))
result.pack()


Button(root,text="C",width=1,height=1,command=show()).place(x=10,y=100)
Button(root,text="C",width=1,height=1,command=show()).place(x=10,y=100)

root.mainloop()
