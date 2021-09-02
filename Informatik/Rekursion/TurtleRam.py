import time
from guppy import hpy


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
    
startTime = time.time()
drawTree(27)
print(27, "|" ,time.time()-startTime)

h = hpy()
print(h.heap())





