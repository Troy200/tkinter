from tkinter import*

root=Tk()
root.geometry("600x600")
root.title("Rock, Paper, Scissors")

title=Label(root, text="Rock, Paper, Scissors", font=("times new roman", 30))
title.pack()

undertitle=Label(root, text="Let's Play", font=("times new roman", 25))
undertitle.pack()

options=Frame(root)
options.pack()

optionstext=Label(options, text="Player Options", font=("times new roman", 20))
optionstext.grid(row=0,column=0)

rockbutton=Button(options, text="Rock", font=("times new roman", 20))
rockbutton.grid(row=0,column=1)


paperbutton=Button(options, text="Paper", font=("times new roman", 20))
paperbutton.grid(row=0,column=2)

scissorsbutton=Button(options, text="Scissors", font=("times new roman", 20))
scissorsbutton.grid(row=0,column=3)

root.mainloop()








