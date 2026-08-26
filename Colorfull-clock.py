from tkinter import *
from time import strftime
import random

root=Tk()
root.geometry("600x400")
root.title("Party Clock")

colors=['red', 'blue', 'green', 'purple', 'orange', 'pink']

def partytime():
    t=strftime("%H:%M:%S")
    c=random.choice(colors)

    Timenow.config(text=t)
    root.config(bg=c)

    Timenow.after(1000,partytime)


Timenow=Label(root, text=strftime("%H:%M:%S"), font=("times new roman", 40))
Timenow.pack(pady=100)


partytime()

root.mainloop()
