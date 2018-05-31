#Sam Krimmel
#5/23/18
#gameOfLife.py - neat

from ggame import *

#CONSTANTS

BH = 10
BW = 10
BB = 20

#FUNCTIONS

def buildBoard():
    boardList = [0]*BH
    for i in range(0,BH):
        boardList[i] = [0]*BW
    return boardList
    

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for x in range(0,BH):
        for y in range(0,BW):
            if data['boardList'][x][y] == 0:
                Sprite(whiteRect,(x*BB,y*BB))
            elif data['boardList'][x][y] == 1:
                Sprite(blackRect,(x*BB,y*BB))

"""
def numNeighbors(row,column):
    
def nextGeneration():
"""
def mouseClick(event):
    if (event.x>((BW*BB/2)-BB) and event.x<((BW*BB/2)-BB)+BB*2) and (event.y<((BH*BB)+30+BH) and event.y>(((BH*BB)+30))):
        nextGeneration()
    elif event.x<(BW*BB) and event.y<(BH*BB):
        if data['boardList'][(event.x//BB)][(event.y//BB)] == 0:
            data['boardList'][(event.x//BB)][(event.y//BB)] = 1
        elif data['boardList'][(event.x//BB)][(event.y//BB)] == 1:
            data['boardList'][(event.x//BB)][(event.y//BB)] = 0
    redrawAll()




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
    nextGenButton = RectangleAsset(BB*2,BH,blackLine,white)
    nextGenText = TextAsset('Next Generation',fill=black, style='bold 50pt Times')
    
    Sprite(nextGenButton,(((BW*BB/2)-BB),(BH*BB)+30))
    Sprite(nextGenText,(((BW*BB/2)-BB),(BH*BB)+30))
    
    redrawAll()
    App().listenMouseEvent('click',mouseClick)
    App().run()
    
    
    