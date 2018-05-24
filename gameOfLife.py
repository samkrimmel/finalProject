#Sam Krimmel
#5/23/18
#gameOfLife.py - neat

from ggame import *

#CONSTANTS

BH = 30
BW = 30
BB = 20

#FUNCTIONS

def buildBoard():
    boardList = [0]*BH
    boardw = [0]*BW
    for i in range(0,12):
        boardList[i] = boardw
    

def redrawAll():
    for x in range(0,BH):
        for y in range(0,BW):
            Sprite(whiteRect,(x*BB,y*BB))
"""
def numNeighbors(row,column):
    
def nextGeneration():
    
def mouseClick(event):
"""



if __name__ == '__main__':
    
    #GRAPHICS
        
        #COLORS
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
    blackLine = LineStyle(1,black)
    whiteRect = RectangleAsset(BB,BB,blackLine,white)
    blackRect = RectangleAsset(BB,BB,blackLine,black)
    
    redrawAll()
    App().run()
    
    
    