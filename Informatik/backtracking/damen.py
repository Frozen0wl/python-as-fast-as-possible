field = []
size = 8 #input('size of field:')
dame = 1
clear = 8
threatened = 0
solutions = []
def createField():
    for i in range(size):
        field.append([])
        for j in range(size):
            field[i].append(clear)

def placeQueen(x, y):
    field[x][y] = dame
    findQueens()

def removeQueen(x, y):
    field[x][y] = clear
    findQueens()
def findQueens():  
    for i in range(size):
        for j in range(size):
            if field[i][j] == dame:
                threatenedFields(i, j)

def threatenedFields(x, y):
    for i in range(size):
        for j in range(size):
            if field[i][j] == threatened:
                field[i][j] == clear
    for i in range(size):
        field[x][i] = threatened
        field[i][y] = threatened

    for i in range(size):
        for j in range(size):
            if x + y == i + j or x - y == i - j:
                field[i][j] = threatened
        field[x][y] = dame       

def printField():
    for i in range(len(field)):
        print(field[i])
    print()

def solve(count = 0):
    printField()
    print(count)
    print()
    if count == size: return True
    for i in range(size):
        for j in range(size):
            if field[i][j] == clear:
                placeQueen(i, j)
                count = count + 1
                if solve(count) == True:
                    return True
                removeQueen(i, j)
                count = count - 1



createField()
findQueens()
printField()
solve()
printField()