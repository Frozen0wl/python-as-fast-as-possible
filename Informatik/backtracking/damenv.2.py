import time
syze = 8
frei = 'W'
dame = 'X'
gui = []
field = []
threatened = 'O'
#creates a gui
def createGui():
    global gui
    gui = []
    for i in range(syze):
        gui.append([])
        for j in range(syze):
            gui[i].append(frei)

createGui()
field = gui

w = 70 # width of each cell


       
def threatenedFields():
    createGui()
    for i in range(syze):
        for j in range(syze):
            if field[i][j] == dame:
                markThreatened(i, j)

def markThreatened(x, y):
    # for i in range(syze):
    #     for j in range(syze):
    #         if field[i][j] == threatened:
    #             field[i][j] == frei
    for i in range(syze):
        gui[x][i] = threatened
        gui[i][y] = threatened

    for i in range(syze):
        for j in range(syze):
            if x + y == i + j or x - y == i - j:
                gui[i][j] = threatened
        gui[x][y] = dame 
def printField():
    for i in range(len(field)):
        print(field[i])
    print()
    
def placeQueen(x, y):
    field[x][y] = dame
    threatenedFields()

def removeQueen(x, y):
    field[x][y] = frei
    threatenedFields()  
                    
def solve(count = 0):

    # time.sleep(1)

    # printField()
    if count == syze: return True
    for i in range(syze):
        for j in range(syze):
            if gui[i][j] == frei:
                placeQueen(i, j)
                count = count + 1
                if solve(count) == True:
                    return True
                removeQueen(i, j)
                count = count - 1
    

solve()
for element in gui:
    print(element)