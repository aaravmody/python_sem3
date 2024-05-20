import tkinter
from tkinter import *
import mysql.connector as ms

myconn=ms.connect(host="localhost",user="root",password="12345678")
print(myconn)

c=myconn.cursor()
#c.execute("create database form")
c.execute("use form")
#c.execute("create table response(name varchar(20),email varchar(30),phone int)")
print("done")

root=Tk()
root.title("Form")
root.geometry("300x300")

def onsub():
    name=n_textbox.get()
    email=e_textbox.get()
    phone=p_textbox.get()
    result=f"{name} \n {email} \n {phone}"
    result_label.config(text=result)
    insertq="Insert into response values(%s,%s,%s)"
    val=(name,email,phone)
    c.execute(insertq,val)
    myconn.commit()
    print("done again")

name_label=Label(root,text="Enter name: ")
name_label.pack()
n_textbox=Entry(root)
n_textbox.pack()


email_label=Label(root,text="Enter email: ")
email_label.pack()
e_textbox=Entry(root)
e_textbox.pack()


phone_label=Label(root,text="Enter phone: ")
phone_label.pack()
p_textbox=Entry(root)
p_textbox.pack()

submit_button=Button(root,text="Submit",command=onsub)
submit_button.pack()

result_label=Label(root,text="")
result_label.pack()


root.mainloop()

c.execute("select * from response")
res=c.fetchall()
for row in res:
    print(row)

