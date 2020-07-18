from tkinter import *
from enum import Enum
master = Tk()

canvas_width = 600
canvas_height = 600
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

xoff = int(canvas_width / 3)
yoff = int(canvas_height / 3)
w.create_line(0, yoff, canvas_width, yoff, fill="#476042", width=3)
w.create_line(0, yoff  * 2, canvas_width, yoff * 2, fill="#476042", width=3)
w.create_line(xoff, 0, xoff, canvas_height, fill="#476042", width=3)
w.create_line(xoff * 2, 0, xoff * 2, canvas_height, fill="#476042", width=3)

currentTurn = 1
gameBoard = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

def drawX(locX, locY):
    w.create_line(xoff * locX + 20, yoff * locY + 20, (xoff * locX) + xoff - 20, (yoff * locY) + yoff - 20, width=3)
    w.create_line((xoff * locX) + xoff - 20, yoff * locY + 20, (xoff * locX) + 20, (yoff * locY) + yoff - 20, width=3)
def drawO(locX, locY):
    w.create_oval(xoff * locX + 20, yoff * locY + 20, (xoff * locX) + xoff - 20, (yoff * locY) + yoff - 20, width=3)
    w.create_oval((xoff * locX) + xoff - 20, yoff * locY + 20, (xoff * locX) + 20, (yoff * locY) + yoff - 20, width=3)

def checkWin():
    global gameBoard
    winner = 0
    if gameBoard[0][0] == gameBoard[1][1] and gameBoard[0][0] == gameBoard[2][2]:
        winner = gameBoard[0][0]
    if gameBoard[2][0] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[0][2]:
        winner = gameBoard[1][1]
    
    for i in range(3):
        # Row
        if gameBoard[i][0] == gameBoard[i][1] and gameBoard[i][0] == gameBoard[i][2]:
            #print("(" + str(0) + ", " + str(i) + "), (" + str(1) + ", " + str(i) + "), (" + str(2) + ", " + str(i) + ")")
            winner = max(gameBoard[i][0], winner)

        # Column
        if gameBoard[0][i] == gameBoard[1][i] and gameBoard[0][i] == gameBoard[2][i]:
            #print("(" + str(i) + ", " + str(0) + "), (" + str(i) + ", " + str(1) + "), (" + str(i) + ", " + str(2) + ")")
            winner = max(gameBoard[0][i], winner)
    
    if winner != 0:
        w.unbind_all("<Button-1>")
        print(winner)
        w.create_text(canvas_width / 2, canvas_height / 2, text="WINNER!", font=('Times', '36', 'bold italic'))

def callback(event):
    global currentTurn
    x = 0
    y = 0

    if event.x < xoff:
        x = 0
    elif event.x < (xoff * 2):
        x = 1
    else:
        x = 2
    
    if event.y < yoff:
        y = 0
    elif event.y < (yoff * 2):
        y = 1
    else:
        y = 2
    
    if gameBoard[y][x] == 0:
        gameBoard[y][x] = currentTurn

        if currentTurn == 1:
            drawX(x, y)
            currentTurn = 2
        else:
            drawO(x, y)
            currentTurn = 1

        checkWin()


w.bind("<Button-1>", callback)

mainloop()