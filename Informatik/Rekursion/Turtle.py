import time
from guppy import hpy


forward = 'forward 30 \n'
back = 'back 30 \n'
right90 = 'right 90 \n'
right45 = 'right 45 \n'
left90 = 'left 90 \n'
left45 = 'left 45 \n'

def drawTree(n):
    if n == 1: return forward + back
    return forward + left45 + drawTree(n-1) + right90 + drawTree(n-1) + left45 + back
    
startTime = time.time()
drawTree(20)
print(20, "|" ,time.time()-startTime)

h = hpy()
print(h.heap())

for i in range(17, 24):
    startTime = time.time()
    drawTree(i) 
    print(i, "|" ,time.time()-startTime)



