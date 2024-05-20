import tkinter as tk

def display():
    name=nameentry.get()
    gender=gendervar.get()
    enter=entervar.get()
    phone=phoneentry.get()
    selected_option = selected_value.get()
    result=f"Name:{name}\nGender:{gender}\nPhone:{phone}\nOption:{selected_option}\nEnter:{enter}"
    resultlabel.config(text=result)
def empty():
    nameentry.delete(0, tk.END)
    phoneentry.delete(0, tk.END)

root=tk.Tk()
root.geometry("300x350")
root.title("GUI using Grid")

namelabel=tk.Label(root,text="Name:")
namelabel.grid(row=1,column=1,padx=10,pady=10)
nameentry=tk.Entry()
nameentry.grid(row=1,column=2,pady=30)

genderlabel=tk.Label(root,text="Gender:")
genderlabel.grid(row=2,column=1)

gendervar=tk.StringVar()
maleradio=tk.Radiobutton(root,text="Male",variable=gendervar,value="Male")
maleradio.grid(row=2,column=2)
femaleradio=tk.Radiobutton(root,text="Female",variable=gendervar,value="Female")
femaleradio.grid(row=2,column=3)

phonelabel=tk.Label(root,text="Phone:")
phonelabel.grid(row=3,column=1,padx=20,pady=10)
phoneentry=tk.Entry()
phoneentry.grid(row=3,column=2,pady=30)

selected_value = tk.StringVar(root)
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
dropdown_menu = tk.OptionMenu(root,selected_value, *options)
dropdown_menu.grid(row=4,column=1)
selected_value.set(options[0])

entervar=tk.StringVar()
entercheck=tk.Checkbutton(root,text="Yes",variable=entervar,onvalue="Yes",offvalue="No")
entercheck.grid(row=5,column=2)

enterbutton1=tk.Button(root,text="Submit",command=display)
enterbutton1.grid(row=6,column=1)

enterbutton2=tk.Button(root,text="Reset",command=empty)
enterbutton2.grid(row=6,column=2)

resultlabel=tk.Label(root,text="")
resultlabel.grid(row=7,column=2,pady=10)
root.mainloop()
