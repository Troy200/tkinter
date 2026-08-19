from tkinter import*
from time import strftime

root=Tk()
root.geometry("600x400")

clock="24"

def clock24():
    global clock
    clock="24"


def clock12():
    global clock
    clock="12"



def H24time():
    if clock == "24":
        t=strftime("%H:%M:%S")
        d=strftime("%A %d %B %Y")

        Timenow.config(text=t)
        Datenow.config(text=d)

        Timenow.after(1000,H24time)

    else:
        t=strftime("%I:%M:%S")
        d=strftime("%A %d %B %Y")
        
        Timenow.config(text=t)
        Datenow.config(text=d)
        
        Timenow.after(1000,H24time)




Timenow=Label(root, text=strftime("%H:%M:%S"),font=("times new roman", 40) )
Timenow.pack()

Datenow=Label(root, text=strftime("%A %d %B %Y"),font=("times new roman", 30) )
Datenow.pack(pady=30)

buttonframe=Frame()
buttonframe.pack(pady=40)

H24=Button(buttonframe, text="24 Hour Time",font=("times new roman", 20), command=clock24)
H24.grid(row=0,column=0)

H12=Button(buttonframe, text="12 Hour Time",font=("times new roman", 20), command=clock12)
H12.grid(row=0,column=1)



H24time()

root.mainloop()