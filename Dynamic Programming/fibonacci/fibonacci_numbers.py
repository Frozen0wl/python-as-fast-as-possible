import time

def fib_num(n):
    if n <= 2: return 1
    return fib_num(n-1) + fib_num(n-2)

for i in range(1, 50):
    previous = time.time()
    print(i, fib_num(i), round(time.time()-previous, 3))

