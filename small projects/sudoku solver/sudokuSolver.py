import DidIFinishmySudoku as possible

counter = 0

board = [[8, 0, 0, 0, 0, 0, 0, 0, 0]
        ,[0, 0, 3, 6, 0, 0, 0, 0, 0]
        ,[0, 7, 0, 0, 9, 0, 2, 0, 0]
        ,[0, 5, 0, 0, 0, 7, 0, 0, 0]
        ,[0, 0, 0, 0, 4, 5, 7, 0, 0]
        ,[0, 0, 0, 1, 0, 0, 0, 3, 0]
        ,[0, 0, 1, 0, 0, 0, 0, 6, 8]
        ,[0, 0, 8, 5, 0, 0, 0, 1, 0]
        ,[0, 9, 0, 0, 0, 0, 4, 0, 0]]

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -") 
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")
def returnNextEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: return (i, j)

def isValid(board, num, pos):
    row = pos[0]
    col = pos[1]    
    for i in range(len(board)):
        if board[row][i] == num and i != col: return False
        if board[i][col] == num and i != row: return False
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    if(returnNextEmpty(board) == None):
        return True
    else:
        row, col = returnNextEmpty(board)
    
    for num in range(1, 10):
        global counter
        counter += 1
        if isValid(board, num, (row, col)):
            
            board[row][col] = num
            if solve(board) == True:
                return True
            board[row][col] = 0
    return False


printBoard(board)
print()
print(possible.done_or_not(board))
solve(board)
printBoard(board)
print()
print(possible.done_or_not(board))
print(counter)