from tkinter import*


root=Tk()
root.geometry("700x700")



board=[]
for row in range(3):
    newrow=[]
    for col in range(3):
        newrow.append(None)
    board.append(newrow)

for row in range(3):
    for col in range(3):
        board [row][col]=Button(root, text="", width=10, height=10 )
        board [row][col].grid(row=row,column=col)
    






root.mainloop()