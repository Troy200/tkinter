from tkinter import*
import random
from tkinter import messagebox


root=Tk()
root.geometry("700x700")
root.title("Lucky Slots")

def spin():
    n1=random.randint(0,9)
    n2=random.randint(0,9)
    n3=random.randint(0,9)

    slot1.config(text=str(n1))
    slot2.config(text=str(n2))
    slot3.config(text=str(n3))

    root.update_idletasks()
    
    if n1==n2==n3:
        messagebox.showinfo("Result","JACKPOT! You win $1000!")
    elif n1==n2 or n1==n3 or n2==n3:
        messagebox.showinfo("Result","Mini Prize! You win $10!")
    else:
        messagebox.showwarning("Result","Bad Luck! Try Again.")


f=Frame(root)
f.pack(pady=100)

slot1=Label(f, text="0", font=("times new roman", 30))
slot1.grid(row=0, column=0)

slot2=Label(f, text="0", font=("times new roman", 30))
slot2.grid(row=0, column=1)

slot3=Label(f, text="0", font=("times new roman", 30))
slot3.grid(row=0, column=2)


spinbutton=Button(root, text="SPIN", font=("times new roman", 20), command=spin)
spinbutton.pack(pady=50)


root.mainloop()