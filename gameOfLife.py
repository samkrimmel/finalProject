#Sam Krimmel
#5/23/18
#gameOfLife.py - neat

from ggame import *

#CONSTANTS

BH = 10
BW = 10
BB = 20

#FUNCTIONS

def buildBoard(): ####DICTIONARY
    boardList = [0]*BH
    boardw = [0]*BW
    for i in range(0,BH):
        boardList[i] = boardw
    return boardList
    

def redrawAll():
    for x in range(0,BH):
        for y in range(0,BW):
            if boardList[x][y] == 0:
                Sprite(whiteRect,(y*BB,x*BB))
            elif boardList[x,y] == 1:
                Sprite(blackRect,(y*BB,x*BB))

"""
def numNeighbors(row,column):
    
def nextGeneration():
    
def mouseClick(event):
    if click on next gen:
        refuse all next clicks
        nextgen
    elif click within board:
        if boardList[black(event.x//BB)-1][(event.y//BB)-1] == 0:
            change to 1
        elif boardList[black(event.x//BB)-1][(event.y//BB)-1] == 1:
            change to 0
        redrawAll()
"""



if __name__ == '__main__':
    
    data = {}
    data['boardList'] = buildBoard()
    
    #GRAPHICS
        
        #COLORS
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
    blackLine = LineStyle(1,black)
    whiteRect = RectangleAsset(BB,BB,blackLine,white)
    blackRect = RectangleAsset(BB,BB,blackLine,black)
    
    redrawAll()
    App().run()
    
    
    