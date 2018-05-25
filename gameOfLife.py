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
    data['boardList'] = [0]*BH
    boardw = [0]*BW
    for i in range(0,BH):
        data['boardList[i]'] = boardw
    

def redrawAll():
    buildBoard()
    for x in range(0,BH):
        for y in range(0,BW):
            if data['boardList[x][y]'] == 0:
                Sprite(whiteRect,(y*BB,x*BB))
            elif data['boardList[x,y]'] == 1:
                Sprite(blackRect,(y*BB,x*BB))

"""
def numNeighbors(row,column):
    
def nextGeneration():
    
def mouseClick(event):
"""



if __name__ == '__main__':
    
    data = {}
    data['boardList'] = []
    
    #GRAPHICS
        
        #COLORS
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
    blackLine = LineStyle(1,black)
    whiteRect = RectangleAsset(BB,BB,blackLine,white)
    blackRect = RectangleAsset(BB,BB,blackLine,black)
    
    redrawAll()
    App().run()
    
    
    