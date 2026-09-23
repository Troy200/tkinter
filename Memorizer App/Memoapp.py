from tkinter import*


root=Tk()
root.geometry("900x700")
root.title("Memorizer")

def addfunc():
    e=entrybox.get()
    lbox.insert(END,e)
    entrybox.delete(0,END)

def clearfunc():
    lbox.delete(0,END)




titlelable=Label( root,text="Memorizer", font=("Arial",40) )
titlelable.grid(row=0, column=0, columnspan=2)

savebutton=Button(root, text="SAVE", font=("Arial",30))
savebutton.grid(row=1, column=0 )

openbutton=Button(root, text="OPEN", font=("Arial",30))
openbutton.grid(row=1, column=1)

entrybox=Entry(root ,width=50)
entrybox.grid(row=2, column=0, columnspan=2)

addbutton=Button(root, text="ADD", font=("Arial",30), command=addfunc)
addbutton.grid(row=3, column=0)

deletebutton=Button(root, text="DELETE", font=("Arial",30))
deletebutton.grid(row=3, column=1)

clearbutton=Button(root, text="CLEAR", font=("Arial",30), command=clearfunc)
clearbutton.grid(row=4, column=0, padx= 200)

lbox=Listbox(root,width=50)
lbox.grid(row=5, column=0, columnspan=2)
for i in range(1,101):
    lbox.insert(END,"LIST"+str(i))
root.mainloop()











