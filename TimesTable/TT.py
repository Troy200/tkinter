from tkinter import *
from tkinter.ttk import *



root=Tk()
root.title("Times Table Display")


def gettables():
    num= numvar.get()
    rangevar= RBvar.get()
    timestable=""

    for i in range(1,rangevar+1,1):
        timestable+=str(num)+" x "+str(i)+" = "+str(num*i)+"\n"

    Resulttable.config(text=timestable)




Title=Label(root, text="Times Table", font=("times new roman", 30))
Title.grid(row=0,column=0)

Num=Label(root, text="Enter Number", font=("times new roman", 20))
Num.grid(row=1,column=0)

numvar=IntVar()

numbox=Combobox(root,textvariable=numvar, font=("times new roman", 20 ))
numbox.grid(row=1,column=1)
numbox['values']= tuple(range(1,101))


Range=Label(root, text="Range", font=("times new roman", 20))
Range.grid(row=1,column=2, padx=10)

RBvar=IntVar()
RB1=Radiobutton(root,text="10",value=10 , variable=RBvar )
RB1.grid(row=2,column=2, padx=10)

RB2=Radiobutton(root,text="20",value=20 , variable=RBvar )
RB2.grid(row=3,column=2, padx=10)

RB3=Radiobutton(root,text="30",value=30 , variable=RBvar )
RB3.grid(row=4,column=2, padx=10)

Gobutton=Button(root,text="Show Table", command=gettables)
Gobutton.grid(row=5,column=2, pady=40)

Resulttable=Label(root, font=("times new roman", 20))
Resulttable.grid(row=5,column=1)
root.mainloop()













