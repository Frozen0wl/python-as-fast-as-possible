import time

start = time.time()
n = 2520
num = 20
while True:
    k = 0
    for i in range(1, num+1):
        if n % i == 0:
            k += 1
    if k  == num:
        print(n)
        break
    else:
        n += 2520
        if(n % 10000 == 0):
            print(n)

end = time.time()

print(end - start)
        