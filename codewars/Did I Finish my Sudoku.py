def done_or_not(board): #board[i][j]
    done = True
    current = []
    for i in range(len(board)):
        if [x for x in range(1, 10)] != sorted(board[i]): return "Try again!"
    
    for i in range(len(board)):
        for j in range(len(board)):
            current.append(board[j][i])
        if [x for x in range(1, 10)] != sorted(current): return "Try again!"
        current.clear()
    
    for starti in range(0, len(board), 3):
        for startj in range(0, len(board), 3):
            for i in range(starti, starti+3):
                for j in range(startj, startj+3):
                    current.append(board[i][j])
            #print(current)d
            if [x for x in range(1, 10)] != sorted(current): return "Try again!"
            current.clear()
    return "Finished!"

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]) == 'Finished!')
                        
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]) == 'Try again!')