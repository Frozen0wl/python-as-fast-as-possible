import time
t = time.time()
j = 0
while j < 1000000000:
    j += 1

print(j, time.time() - t)    