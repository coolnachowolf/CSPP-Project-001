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
    data["number of rows"]=10
    data["number of cols"]=10
    data["board size"]=500
    data["number of ships"]=5
    data["cellsize"]=data["board size"]/data["number of rows"]
    data["computer"]=emptyGrid(data["number of rows"],data["number of cols"])
    data["user"]=emptyGrid(data["number of rows"],data["number of cols"])
    data["temporary ship"]=[]
    data["numships"]=0
    data["winner"]=None
    data["max num of turns"]=50
    data["current num of turns"]=0
    addShips(data["computer"],data["number of ships"])
'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user"],True)
    drawGrid(data,compCanvas,data["computer"],False)
    drawShip(data,userCanvas,data["temporary ship"])
    drawGameOver(data,userCanvas)


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    print(event,type(event))
    if event.char=='\r':
        makeModel(data)


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if data["winner"]==None:
        if board=="comp":
            if data["numships"]==5:
                cell=getClickedCell(data,event)
                runGameTurn(data,cell[0],cell[1])
        if data["numships"]<5:
            if board=="user":
                cell=getClickedCell(data,event)
                clickUserBoard(data,cell[0],cell[1])
                      
#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for row in range (rows):
        grid.append([])
        d=grid[row]
        for col in range(cols):
            d.append(EMPTY_UNCLICKED)
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row=random.randint(1,8)
    col=random.randint(1,8)
    align=random.randint(0,1)
    if align==0:
        ship=[[row-1,col],[row,col],[row+1,col]]
    else:
        ship=[[row,col-1],[row,col],[row,col+1]]
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in range(len(ship)):
        x=ship[i][0]
        y=ship[i][1]
        if grid[x][y]!=EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    j=0
    while j<numShips:
        ship=createShip()
        if checkShip(grid,ship)==True:
            for i in range(len(ship)):
                x=ship[i][0]
                y=ship[i][1]
                grid[x][y]=SHIP_UNCLICKED
            j+=1

    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    i=data["cellsize"]
    for row in range(data["number of rows"]):
        for col in range(data["number of cols"]):
            if grid[row][col]==SHIP_UNCLICKED:
                if showShips==True:
                    canvas.create_rectangle(col*i,row*i,data["cellsize"]+col*i,data["cellsize"]+row*i,fill="#ffff00")
                elif showShips==False:
                    canvas.create_rectangle(col*i,row*i,data["cellsize"]+col*i,data["cellsize"]+row*i,fill="blue")
            elif grid[row][col]==SHIP_CLICKED:
                canvas.create_rectangle(col*i,row*i,data["cellsize"]+col*i,data["cellsize"]+row*i,fill="red")
            elif grid[row][col]==EMPTY_CLICKED:
                canvas.create_rectangle(col*i,row*i,data["cellsize"]+col*i,data["cellsize"]+row*i,fill="white")
            else:
                canvas.create_rectangle(col*i,row*i,data["cellsize"]+col*i,data["cellsize"]+row*i,fill="blue")
        
    


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    if ship[0][1]==ship[1][1]==ship[2][1]:
        x=sorted([ship[0][0],ship[1][0],ship[2][0]])
        if x[1]-x[0]==1:
            if x[2]-x[1]==1:
                return True
    
    return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    if ship[0][0]==ship[1][0]==ship[2][0]:
        x=sorted([ship[0][1],ship[1][1],ship[2][1]])
        if x[1]-x[0]==1:
            if x[2]-x[1]==1:
                return True
    
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    row=int((event.y)/(data["board size"]/data["number of rows"]))
    col=int((event.x)/(data["board size"]/data["number of rows"]))
    return [row,col]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    size=data["cellsize"]
    for i in range(len(ship)):
        canvas.create_rectangle(ship[i][1]*size,ship[i][0]*size,size+ship[i][1]*size,size+ship[i][0]*size,fill="white")


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid,ship):
        if isVertical(ship):
            return True
        elif isHorizontal(ship):
            return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["user"],data["temporary ship"]):
        ship=data["temporary ship"]
        for i in ship:
            data["user"][i[0]][i[1]]=SHIP_UNCLICKED
        data["numships"]+=1
    else:
        print("Error:ship is not valid")
    data["temporary ship"]=[]

'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if [row,col] not in data["temporary ship"]:
        data["temporary ship"].append([row,col])
        if len(data["temporary ship"])==3:
            placeShip(data)        



### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):

        if board[row][col]==SHIP_UNCLICKED:
            board[row][col]=SHIP_CLICKED
        elif board[row][col]==EMPTY_UNCLICKED:
            board[row][col]=EMPTY_CLICKED
        if isGameOver(board):
            data["winner"]=player


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if data["computer"][row][col]==SHIP_UNCLICKED or data["computer"][row][col]==EMPTY_UNCLICKED:
        updateBoard(data,data["computer"],row,col,"user")
        guess=getComputerGuess(data["user"])
        updateBoard(data,data["user"],guess[0],guess[1],"comp")
        data["current num of turns"]+=1
        if data["current num of turns"]==data["max num of turns"]:
            data["winner"]="draw"



'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    row=random.randint(0,9)
    col=random.randint(0,9)
    while board[row][col]==SHIP_CLICKED or board[row][col]==EMPTY_CLICKED:
        row=random.randint(0,9)
        col=random.randint(0,9)
    return [row,col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range(len(board)):
        row=board[i]
        for j in range(len(row)):
            if row[j]==SHIP_UNCLICKED:
                return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"]=="user":
        canvas.create_text(250, 220, text="You won", font="Arial 40",fill="pink")
        canvas.create_text(250, 320, text="Congratulations!", font="Arial 40",fill="pink")
        canvas.create_text(250, 420, text="Press Enter to play again", font="Arial 25",fill="pink")
    if data["winner"]=="comp":
        canvas.create_text(250, 220, text="You lose :(", font="Arial 40",fill="pink")
        canvas.create_text(250, 320, text="Press Enter to play again", font="Arial 25",fill="pink")
    if data["winner"]=="draw":
        canvas.create_text(250, 220, text="Out of moves. Draw", font="Arial 40",fill="pink")
        canvas.create_text(250, 320, text="Press Enter to play again", font="Arial 25",fill="pink")



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
    # test.testEmptyGrid()
    # test.testCreateShip()
    # test.testCheckShip()
    # test.testAddShips()
    # test.testMakeModel()
    # test.testIsVertical()
    # test.testIsHorizontal()
    # test.testGetClickedCell()
    # test.testShipIsValid()
    # test.testUpdateBoard()
    # test.testGetComputerGuess()
    # test.testIsGameOver()
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)