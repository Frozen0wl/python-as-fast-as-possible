def done_or_not(board): #board[i][j]
    current = []
    for i in range(len(board)):
        if [x for x in range(1, 10)] != sorted(board[i]): return False
    
    for i in range(len(board)):
        for j in range(len(board)):
            current.append(board[j][i])
        if [x for x in range(1, 10)] != sorted(current): return False
        current.clear()
    
    for starti in range(0, len(board), 3):
        for startj in range(0, len(board), 3):
            for i in range(starti, starti+3):
                for j in range(startj, startj+3):
                    current.append(board[i][j])
            #print(current)d
            if [x for x in range(1, 10)] != sorted(current): return False
            current.clear()
    return True

