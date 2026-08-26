from tkinter import*
import random
from tkinter import messagebox


root=Tk()
root.geometry("700x700")

thenumber=random.randint(1,20)
tries=0

def namecheck():
    y=inna.get()
    if len(inna.get())>= 1:
        messagebox.showinfo("The Rules","Hello " +y + " I am thinking of a number between 1 and 20 try to guess." )
        b2.config(state=NORMAL)

    else:
        messagebox.showinfo("Error info","Please enter your name" )

def numbercheck():
    n=int(innu.get())
    global tries
    if len(innu.get())>= 1:
        if n==thenumber:
           messagebox.showinfo("Result","Great you guessed the number in " + str(tries)+ " tries!" ) 
        elif n> thenumber:
           messagebox.showinfo("Feedback","Thats too high!" )
           tries=tries+1
        elif n<thenumber:
            messagebox.showinfo("Feedback","Thats too low!" )
            tries=tries+1
    else:
        messagebox.showinfo("Feedback","Please enter a number." )
    
           
           





welcome=Label(root, text="Welcome to GTN !!!" ,font=("times new roman", 50))
welcome.pack()

f=Frame(root)
f.pack(pady=50)

n=Label(f, text="Name -> " ,font=("times new roman", 20))
n.grid(row=0, column=0)
n=Label(f, text="Number -> " ,font=("times new roman", 20))
n.grid(row=1, column=0)

inna=Entry(f)
inna.grid(row=0, column=1)
innu=Entry(f)
innu.grid(row=1, column=1)

b1=Button(f, text="☑️" ,font=("times new roman", 20), command= namecheck)
b1.grid(row=0, column=2)
b2=Button(f, text="Guess" ,font=("times new roman", 20), state=DISABLED, command=numbercheck)
b2.grid(row=1, column=2)






root.mainloop()