from tkinter import*
import random
from tkinter import messagebox

root=Tk()
root.geometry("600x600")
root.title("Math Quiz")

score=0
questionnum=0

num1=0
num2=0
answer=0

def newquestion():
    global num1, num2, answer, questionnum
    questionnum=questionnum+1

    num1=random.randint(1,20)
    num2=random.randint(1,20)
    answer=num1+num2

    questiontitle.config(text= str(num1) + " + " + str(num2) + " = ?" )
    qnum.config(text= "Question " + str(questionnum) )
    answerentry.delete(0,END)


def checkanswer():
    global score
    a=answerentry.get()

    if len(a)>=1:
        if int(a)==answer:
            messagebox.showinfo("Result","Correct! Well done." )
            score=score+1
            scorelabel.config(text= "Score " + str(score) )
        else:
            messagebox.showinfo("Result","Wrong! The answer was " + str(answer) )

        newquestion()

    else:
        messagebox.showinfo("Error","Please enter an answer." )



title=Label(root, text="Math Quiz", font=("times new roman", 30))
title.pack()

qnum=Label(root, text="Question 1", font=("times new roman", 20))
qnum.pack(pady=10)

questiontitle=Label(root, text="? + ? = ?", font=("times new roman", 40))
questiontitle.pack(pady=30)

answerentry=Entry(root, font=("times new roman", 30))
answerentry.pack(pady=10)

submitbutton=Button(root, text="Submit", font=("times new roman", 20), command=checkanswer)
submitbutton.pack(pady=20)

scorelabel=Label(root, text="Score 0", font=("times new roman", 20))
scorelabel.pack(pady=20)

newquestion()

root.mainloop()