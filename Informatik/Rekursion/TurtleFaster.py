import time

forward = 'forward 30 \n'
back = 'back 30 \n'
right90 = 'right 90 \n'
right45 = 'right 45 \n'
left90 = 'left 90 \n'
left45 = 'left 45 \n'

def drawTree(n, memo = {}):
    if n in memo: return memo[n]
    if n == 1: return forward + back
    else: memo[n] = forward + left45 + drawTree(n-1) + right90 + drawTree(n-1) + left45 + back
    return memo[n]

for i in range(17, 29): #28 braucht 12gb ram xD
    startTime = time.time()
    drawTree(i)
    print(i, "|" ,time.time()-startTime)



