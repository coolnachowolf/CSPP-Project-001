"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows_cols"] = 10
    data["board_size"] = 500
    data["numShips"] = 5
    data["cell_size"] = (data["board_size"])/(data["rows_cols"])
    data["empty_ship"] = []
    data["computer_board"] = emptyGrid(data["rows_cols"],data["rows_cols"])
    data["user_board"] = emptyGrid(data["rows_cols"],data["rows_cols"])
    data["computer_board"] = addShips(data["computer_board"],data["numShips"])
    data["temp_ship"] = []
    data["ships"] = 0
    data["winner"] = None
    data["max_turns"] = 50
    data["turns"] = 0
    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, userCanvas, data["user_board"], True)
    drawGrid(data, compCanvas, data["computer_board"], False)
    drawGameOver(data, userCanvas)
    drawShip(data, userCanvas, data["temp_ship"])
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym == "Return":
        makeModel(data)
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    cells = getClickedCell(data, event)
    if data["winner"] == None:
        if board == "user":
            clickUserBoard(data, cells[0], cells[1])
        if board == "comp" and data["ships"] == 5:
            runGameTurn(data, cells[0], cells[1])
    pass
    
#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    lst = []
    for i in range(rows):
        lst1 = []
        for j in range(cols):
            lst1.append(EMPTY_UNCLICKED)
        lst.append(lst1)
    return lst


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    ship = []
    row = random.randint(1,8)
    col = random.randint(1,8)
    step = random.randint(0,1)
    if step == 0: # 0 is vertical
        for i in range(row-1,row+2):
            ship.append([i,col])
    else:
        for i in range(col-1,col+2):
            ship.append([row,i])
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in range(len(ship)):
        if grid[ship[i][0]][ship[i][1]] != EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    board = grid
    count = 0
    while count < numShips:
        ship = createShip()
        if checkShip(board, ship) == True:
            for i in range(len(ship)):
                board[ship[i][0]][ship[i][1]] = SHIP_UNCLICKED
            count += 1
    return board


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(data["rows_cols"]):
        for j in range(data["rows_cols"]):
            a = data["cell_size"]*i 
            b = data["cell_size"]*j
            c = data["cell_size"] + a
            d = data["cell_size"] + b
            canvas.create_rectangle(a, b, c, d, fill="blue")
            #if showShips == True:
            if grid[i][j] == SHIP_UNCLICKED:
                if showShips == True:
                    canvas.create_rectangle(a, b, c, d, fill = "yellow")
                else: 
                    canvas.create_rectangle(a, b, c, d, fill="blue")
            if grid[i][j] == SHIP_CLICKED:
                canvas.create_rectangle(a, b, c, d, fill = "red")
            if grid[i][j] == EMPTY_CLICKED:
                canvas.create_rectangle(a, b, c, d, fill = "white")
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    x = sorted(ship)
    y = x[2][0]-x[1][0]
    z = x[1][0]-x[0][0]
    if(x[0][1]==x[1][1]==x[2][1]):
        if(y == 1):
            if(z==1):
                return True
    return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    x = sorted(ship)
    y = x[2][1]-x[1][1]
    z = x[1][1]-x[0][1]
    if(x[0][0]==x[1][0]==x[2][0]):
        if(y == 1):
            if(z==1):
                return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    y = int(event.y/data["cell_size"])
    x = int(event.x/data["cell_size"])
    return [x,y]
    

'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
        a = data["cell_size"] * ship[i][0]
        b = data["cell_size"] * ship[i][1]
        c = data["cell_size"] + a
        d = data["cell_size"] + b
        canvas.create_rectangle(a, b, c ,d, fill="white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid, ship):
        if isHorizontal(ship):
            return True
        elif isVertical(ship):
            return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["user_board"], data["temp_ship"]):
        ship = data["temp_ship"]
        for i in range(len(ship)):
            data["user_board"][ship[i][0]][ship[i][1]] = SHIP_UNCLICKED
        data["ships"] += 1
    else:
        print("ERROR: Invalid Ship!")
    data["temp_ship"] = []
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["ships"] == 5:
        if [row,col] in data["temp_ship"]:
            return None
    else:
        data["temp_ship"].append([row,col])
        if (len(data["temp_ship"]) == 3):
            placeShip(data)
    if data["ships"] == 5:
        print("Game Ready!")

### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col] == SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED
    elif board[row][col] == EMPTY_UNCLICKED:
        board[row][col] = EMPTY_CLICKED
    if isGameOver(board) == True:
        data["winner"] = player


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if (data["computer_board"][row][col] == SHIP_UNCLICKED) or (data["computer_board"][row][col] == EMPTY_UNCLICKED):
        updateBoard(data, data["computer_board"], row, col, "user")
        guess = getComputerGuess(data["user_board"])
        updateBoard(data, data["user_board"], guess[0], guess[1], "comp")
        data["turns"] += 1
        if data["turns"] == data["max_turns"]:
            data["winner"] = "draw"
    return



'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    row = random.randint(0,9)
    col = random.randint(0,9)
    while board[row][col] == SHIP_CLICKED or board[row][col] == EMPTY_CLICKED:
        row = random.randint(0,9)
        col = random.randint(0,9)
    return [row, col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == SHIP_UNCLICKED:
                return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"] == "user":
        canvas.create_rectangle(0, 150, 500, 300, fill='white', outline='black')
        canvas.create_text(250, 170, text="You Won", fill="hotpink4", font=('Book Antiqua',40, 'bold'))
        canvas.create_text(250, 220, text="Congratulations User!", fill="hotpink4", font=('Book Antiqua', 30, 'bold'))
        canvas.create_text(250, 270, text="Press ENTER to play again", fill="hotpink4", font=('Book Antiqua', 30, 'bold'))
    elif data["winner"] == "comp":
        canvas.create_rectangle(0, 150, 500, 300, fill='white', outline='black')
        canvas.create_text(250, 170, text="You Lost", fill="hotpink4", font=('Book Antiqua', 40, 'bold'))
        canvas.create_text(250, 220, text="Computer Won", fill="hotpink4", font=('Book Antiqua', 30, 'bold'))
        canvas.create_text(250, 270, text="Press ENTER to play again", fill="hotpink4", font=('Book Antiqua', 30, 'bold'))
    elif data["winner"] == "draw":
        canvas.create_rectangle(0, 150, 500, 300, fill='white', outline='black')
        canvas.create_text(250, 170, text="Draw Game", fill="hotpink4", font=('Book Antiqua', 40, 'bold'))
        canvas.create_text(250, 220, text="Out of Moves!", fill="hotpink4", font=('Book Antiqua', 30, 'bold'))
        canvas.create_text(250, 270, text="Press ENTER to play again", fill="hotpink4", font=('Book Antiqua', 30, 'bold'))


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)

