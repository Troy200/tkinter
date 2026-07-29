from tkinter import*

root=Tk()
root.geometry("600x400")

def convert():
    kg=float(kginbox.get())
    g=kg*1000
    lbs=kg*2.20462
    oz=kg*35.274
     
    Gramin.delete(0,END) 
    Gramin.insert(0,g)
    Poundin.delete(0,END)
    Poundin.insert(0,lbs)
    Ouncein.delete(0,END)
    Ouncein.insert(0,oz)







Enterlable=Label(root, text="Enter Kg's",font=("times new roman", 30) )
Enterlable.grid(row=0,column=0, columnspan=2)

kginbox=Entry(root)
kginbox.grid(row=0,column=2)


Gram=Label(root, text="Grams",font=("times new roman", 20) )
Gram.grid(row=1,column=0)


Gramin=Entry(root)
Gramin.grid(row=2,column=0)

Pound=Label(root, text="Pounds",font=("times new roman", 20) )
Pound.grid(row=1,column=1)

Poundin=Entry(root)
Poundin.grid(row=2,column=1)

Ounce=Label(root, text="Ounces",font=("times new roman", 20) )
Ounce.grid(row=1,column=2)

Ouncein=Entry(root)
Ouncein.grid(row=2,column=2)

convbutton=Button(root, text="convert",font=("times new roman", 20), command=convert)
convbutton.grid(row=3,column=1)








root.mainloop()