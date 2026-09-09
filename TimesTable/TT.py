from tkinter import *
from tkinter.ttk import *



root=Tk()
root.geometry("600x600")
root.title("Times Table Display")



Title=Label(root, text="Times Table", font=("times new roman", 30))
Title.grid(row=0,column=0)

Num=Label(root, text="Enter Number", font=("times new roman", 20))
Num.grid(row=1,column=0)

numop=IntVar()

numbox=Combobox(root,textvariable=numop, font=("times new roman", 20 ))
numbox.grid(row=1,column=1)
numbox['values']= tuple(range(1,101))


Range=Label(root, text="Range", font=("times new roman", 20))
Range.grid(row=1,column=2, padx=10)




root.mainloop()













