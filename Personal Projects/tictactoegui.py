from tkinter import *
import numpy as np
import random
import time

grid = np.empty(shape=(3, 3), dtype=str)
notwon = True
root = Tk()
root.title('Tic Tac Toe')
root.iconbitmap

clicked = True
count = 0

print(grid)
x = True


def b_click(i, j, b):
    global x
    if x:
        if grid[i, j] != "X" and grid[i, j, ] != 'O':
            grid[i, j] = "X"
            print(grid)
            b["text"] = 'X'
            b["fg"] = "Red"
            x = False
        elif grid[i, j] == 'X' or grid[i, j] == 'O':
            print("Invalid selection, choose another space")
    if x == False:
        if grid[i, j] != "X" and grid[i, j, ] != 'O':
            grid[i, j] = "O"
            print(grid)
            b["text"] = 'O'
            b["fg"] = "Green"
            x = True
            X = False
        elif grid[i, j] == 'X' or grid[i, j] == 'O':
            print("Invalid selection, choose another space")


def pcturn():
    random.randint(0,)


b1 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", fg="Red", command=lambda: b_click(0, 0, b=b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(0, 1, b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(0, 2, b3))
b4 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(1, 0, b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(1, 1, b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(1, 2, b6))
b7 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(2, 0, b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(2, 1, b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(2, 2, b9))
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


root.mainloop()
