from tkinter import*
import random

root=Tk()
root.geometry("600x600")
root.title("Rock, Paper, Scissors")

choices=["rock","paper","scissors"]

ps=0
cs=0
def play(playerchoice):
    global ps, cs
    input.config(text= "Your input = " + playerchoice )
    cc=random.choice(choices)
    cinput.config(text= " Computer input = " + cc )

    if cc == playerchoice:
        undertitle.config(text= "It's a Tie")

    elif cc == "rock" and playerchoice== "paper":
        undertitle.config(text= "Player Wins")
        ps= ps+1
        score.config(text= "Your score "+ str(ps) )

    elif cc == "rock" and playerchoice== "scissors":
        undertitle.config(text= "Computer Wins")
        cs= cs+1
        cscore.config(text= "Computer score "+ str(cs) )

    elif cc == "paper" and playerchoice== "rock":
        undertitle.config(text= "Computer Wins")
        cs= cs+1
        cscore.config(text= "Computer score "+ str(cs) )

    elif cc == "paper" and playerchoice== "scissors":
        undertitle.config(text= "Player Wins")
        ps= ps+1
        score.config(text= "Your score "+ str(ps) )

    elif cc == "scissors" and playerchoice== "rock":
        undertitle.config(text= "Player Wins")
        ps= ps+1
        score.config(text= "Your score "+ str(ps) )

    elif cc == "scissors" and playerchoice== "paper":
        undertitle.config(text= "Computer Wins")
        cs= cs+1
        cscore.config(text= "Computer score "+ str(cs) )

title=Label(root, text="Rock, Paper, Scissors", font=("times new roman", 30))
title.pack()

undertitle=Label(root, text="Let's Play", font=("times new roman", 25))
undertitle.pack()

options=Frame(root)
options.pack(pady=40)

optionstext=Label(options, text="Player Options", font=("times new roman", 20))
optionstext.grid(row=0,column=0)

rockbutton=Button(options, text="Rock", font=("times new roman", 20), command=lambda:play(choices[0]))
rockbutton.grid(row=0,column=1)


paperbutton=Button(options, text="Paper", font=("times new roman", 20), command=lambda:play(choices[1]))
paperbutton.grid(row=0,column=2)

scissorsbutton=Button(options, text="Scissors", font=("times new roman", 20), command=lambda:play(choices[2]))
scissorsbutton.grid(row=0,column=3)


output=Frame(root)
output.pack(pady=40)

input=Label(output, text="Your input ____", font=("times new roman", 20))
input.grid(row=0,column=0)

score=Label(output, text="Your score ___", font=("times new roman", 20))
score.grid(row=0,column=1)

cinput=Label(output, text="Computer input ____", font=("times new roman", 20))
cinput.grid(row=1,column=0)

cscore=Label(output, text="Computer score ___", font=("times new roman", 20))
cscore.grid(row=1,column=1)


root.mainloop()








