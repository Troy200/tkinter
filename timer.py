from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
root.title("Timer")

totals=0
def starttime():
    global totals
    sb.config(state=DISABLED)
    h.config(state=DISABLED)
    m.config(state=DISABLED)
    s.config(state=DISABLED)
    totals= (int(hour.get())* 3600) + (int(min.get())* 60) + (int(sec.get()))

    countdown()


def countdown():
    global totals
    mi,se=divmod(totals,60)
    ho,mi=divmod(mi,60)
    hour.set(f"{ho:02d}")
    min.set(f"{mi:02d}")
    sec.set(f"{se:02d}")
    if totals==0:
        messagebox.showinfo("Time's Up","Time's Up" )
        sb.config(state=NORMAL)
        h.config(state=NORMAL)
        m.config(state=NORMAL)
        s.config(state=NORMAL)
        return
    totals=totals-1
    root.after(1000,countdown)

hour=StringVar()
hour.set("00")
h=Entry(root,textvariable=hour, width=2, font=("times new roman", 50) )
h.place(x=220 , y=150)

min=StringVar()
min.set("00")
m=Entry(root,textvariable=min, width=2, font=("times new roman", 50) )
m.place(x=300 , y=150)


sec=StringVar()
sec.set("00")
s=Entry(root,textvariable=sec, width=2, font=("times new roman", 50) )
s.place(x=380 , y=150)

sb=Button(root, text=("start timer"),font=("times new roman", 30), command= starttime)
sb.place(x=250 , y=250)

root.mainloop()