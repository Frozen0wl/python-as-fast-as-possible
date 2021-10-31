field = []
clear = 'O'
dame = 'X'


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

def solve(count = 0):
    if count == size: return True
    for i in range(size):
        for j in range(size):
            if isPossible(i, j): 
                toggle(i, j) 
                count += 1
                if solve(count) == True:
                    return True
                toggle(i, j, False)
                count -= 1


for i in range(100):
    size = i
    createField()
    solve()
    printField()
    print()