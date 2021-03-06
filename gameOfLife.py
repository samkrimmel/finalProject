#Sam Krimmel
#5/23/18
#gameOfLife.py - Conway's Laggy Game of Life

from ggame import *

#CONSTANTS

BH = 10 #board height
BW = 10 #width
BB = 20 #cell size

#FUNCTIONS

def buildBoard(): #makes a list matrix that represents the board
    boardList = [0]*BH #make a list with BH zeros
    for i in range(0,BH): #for every zero
        boardList[i] = [0]*BW #make BW zeros
    return boardList 
    

def redrawAll(): #sprites the right board
    for item in App().spritelist[:]: #clears everything
        item.destroy()
    for x in range(0,BH):
        for y in range(0,BW):
            if data['boardList'][x][y] == 0:
                Sprite(whiteRect,(x*BB,y*BB)) #puts white rect where there are zeros (dead)
            elif data['boardList'][x][y] == 1:
                Sprite(blackRect,(x*BB,y*BB)) #puts black rect where there are ones (alive)
    Sprite(nextGenButton,(((BW*BB/2)-2*BB),(BH*BB)+30)) #sprites the button
    Sprite(nextGenText,(((BW*BB/2)-2*BB),(BH*BB)+30)) #sprites the button text


def numNeighbors(row,col): #checks how many neighbors are around a cell (tricky)
    nb = 0 
    if col != 0: #as long as you can check left
        if data['boardList'][row][col-1] == 1: #checks left
            nb += 1
    if row != 0:
        if data['boardList'][row-1][col] == 1: #checks top
            nb += 1
    if col != BW-1:
        if data['boardList'][row][col+1] == 1: #checks right
            nb += 1
    if row != BH-1:
        if data['boardList'][row+1][col] == 1: #checks bottom
            nb += 1
    if row != 0 and col != 0:
        if data['boardList'][row-1][col-1] == 1: #checks top left
            nb += 1
    if row != BH-1 and col != BW-1:
        if data['boardList'][row+1][col+1] == 1: #checks bottom right
            nb += 1
    if row != 0 and col != BW-1:
        if data['boardList'][row-1][col+1] == 1: #checks top right
            nb += 1
    if row != BH-1 and col != 0:
        if data['boardList'][row+1][col-1] == 1: #checks bottom left
            nb += 1
    return nb #returns number of neighbors for an inputted cell

def nextGeneration(): #Sprites the next generation of cells on the board according to the rules of the game
    
    data['newBoardList'] = buildBoard() #resets new list
    for c in range(0,BW): 
        for r in range(0,BH):
            boxnb = numNeighbors(r,c) #finds the number of neighbors for the cell in loop
            if data['boardList'][r][c] == 1: #concerning living cells
                if boxnb < 2 or boxnb > 3: 
                    data['newBoardList'][r][c] = 0 #If the cell has less than 2 neighbors or more than 3, it is put in new list as dead
                if boxnb == 2 or boxnb == 3:
                    data['newBoardList'][r][c] = 1 #If the cell has 2 or 3 neighbors, it is put in new list as living
            elif data['boardList'][r][c] == 0: #concerning dead cells
                if boxnb == 3:
                    data['newBoardList'][r][c] = 1 #If the dead cell has exactly three neighbors, alive in new list
    data['boardList'] = data['newBoardList'] #make the new list the old list
    redrawAll() #remakes the board

def mouseClick(event): #deals with all the mouseclicks and user inputs
    if (event.x>((BW*BB/2)-2*BB) and event.x<((BW*BB/2)-2*BB)+BB*4) and (event.y<((BH*BB)+30+BH) and event.y>(((BH*BB)+30))):
        nextGeneration() #If you hit the next gen button, call the next gen function
    elif event.x<(BW*BB) and event.y<(BH*BB): #if your click is within a cell on the board
        if data['boardList'][(event.x//BB)][(event.y//BB)] == 0: #if the cell is white
            data['boardList'][(event.x//BB)][(event.y//BB)] = 1 #make it black in the list
        elif data['boardList'][(event.x//BB)][(event.y//BB)] == 1: #if the cell is black
            data['boardList'][(event.x//BB)][(event.y//BB)] = 0 #make it white in the list
    redrawAll() #remake the board (because the board is remade after every click, it is not the most responsive game)




if __name__ == '__main__':
    
    #DICTIONARY
    data = {}
    data['boardList'] = buildBoard() 
    data['newBoardList'] = buildBoard()
    
    #GRAPHICS
        
        #COLORS
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
        #ITEMS
    blackLine = LineStyle(1,black)
    whiteRect = RectangleAsset(BB,BB,blackLine,white)
    blackRect = RectangleAsset(BB,BB,blackLine,black)
    nextGenButton = RectangleAsset(BB*4,BH*2,blackLine,white)
    nextGenText = TextAsset('Next Gen',fill=black, style='bold 13pt Times')
    
    redrawAll()
    App().listenMouseEvent('click',mouseClick)
    App().run()
    
    