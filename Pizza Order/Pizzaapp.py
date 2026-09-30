from tkinter import *
from tkinter.ttk import *


root=Tk()
root.title("Pizza App")


def order():
    pizza= pizzavar.get()
    num= numvar.get()
    size= sizevar.get()

    if size=="S":
        sizetext="Small"
    elif size=="M":
        sizetext="Medium"
    else:
        sizetext="Large"

    result.config(text= "You ordered " + str(num) + " " + pizza + " " + sizetext + " Size Pizza(s)" )



Title=Label(root, text="Welcome to Pizza Hut", font=("times new roman", 30, "bold"))
Title.grid(row=0,column=0,columnspan=3,pady=30)

Pizzalabel=Label(root, text="Select Your Fav Pizza:", font=("times new roman", 15))
Pizzalabel.grid(row=1,column=0,pady=15)

pizzavar=StringVar()
pizzabox=Combobox(root,textvariable=pizzavar, font=("times new roman", 15), state="readonly")
pizzabox.grid(row=1,column=1)
pizzabox['values']=("Margherita","Pepperoni","BBQ Chicken","Veggie")



Qtylabel=Label(root, text="Enter Quantity:", font=("times new roman", 15))
Qtylabel.grid(row=2,column=0,pady=15)

numvar=IntVar()
numbox=Combobox(root,textvariable=numvar, font=("times new roman", 15))
numbox.grid(row=2,column=1)
numbox['values']= tuple(range(1,11))


Sizelabel=Label(root, text="Select Size:", font=("times new roman", 15))
Sizelabel.grid(row=3,column=0,pady=15)

sizevar=StringVar()
sizevar.set("M")

sizeframe=Frame(root)
sizeframe.grid(row=3,column=1)

RBS=Radiobutton(sizeframe,text="S",value="S", variable=sizevar)
RBS.grid(row=0,column=0,padx=10)

RBM=Radiobutton(sizeframe,text="M",value="M", variable=sizevar)
RBM.grid(row=0,column=1,padx=10)

RBL=Radiobutton(sizeframe,text="L",value="L", variable=sizevar)
RBL.grid(row=0,column=2,padx=10)

Orderbutton=Button(root,text="Order", command=order)
Orderbutton.grid(row=4,column=0,columnspan=3,pady=20)

result=Label(root, text="", font=("times new roman", 15, "bold"), foreground="red")
result.grid(row=5,column=0,columnspan=3,pady=10)

root.mainloop()
