from random import random
from math import sqrt
import time
n = 1
while True:
    t = time.time()
    I = 0
    for i in range(n):
        x = random()
        y = random()
        if x*x+y*y<= 1:
            I+=1 
        r = sqrt(x**2+y**2)
        if r < 1: I += 1

    print(4*I/n, time.time()-t)
    n = n*10