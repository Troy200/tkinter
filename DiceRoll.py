from tkinter import *
import random

root=Tk()
root.geometry("400x400")
root.title("Dice Roller")

def roll():
    number=random.randint(1,6)
    dicelabel.config(text=str(number))

title=Label(root, text="Roll the Dice!", font=("times new roman", 25))
title.pack(pady=30)

dicelabel=Label(root, text="1", font=("times new roman", 80))
dicelabel.pack(pady=20)

rollbutton=Button(root, text="ROLL", font=("times new roman", 15), command=roll)
rollbutton.pack(pady=30)

root.mainloop()