field = []
clear = 'O'
dame = 'X'
counter = 0
solutions = []

def createField():
    global field
    field = []
    for i in range(size):
        field.append([])
        for j in range(size):
            field[i].append(clear)

def printField():
    for i in range(size):
        for j in range(size):
            print(field[i][j], end = " ")
        print()

def isPossible(x, y):
    for i in range(size):
        if field[x][i] == dame or field[i][y] == dame:
            return False
        
    for i in range(size):
        for j in range(size):
            if x + y == i + j or x - y == i - j:
                if field[i][j] == dame: return False
    return True

def toggle(x, y, bool = True):
    if bool: field[x][y] = dame
    else: field[x][y] = clear

def nQueen(mat, r):
 
    # if `N` queens are placed successfully, print the solution
    if r == size:
        printField()
        return
 
    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(size):
 
        # if no two queens threaten each other
        if isPossible(r, i):
            # place queen on the current square
            mat[r][i] = 'Q'
 
            # recur for the next row
            nQueen(mat, r + 1)
 
            # backtrack and remove the queen from the current square
            mat[r][i] = '–'
size = 5
createField()
nQueen(field, 0)
printField()
# for i in range(100):
#     size = i
#     createField()
#     solve()
#     printField()
#     print()
