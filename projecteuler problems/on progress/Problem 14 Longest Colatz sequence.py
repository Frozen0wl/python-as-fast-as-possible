import time

t = time.time()

counter = 1
longest = 0
complete = 0
for i in range(1, 1000000):
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        counter += 1

        if counter > longest:
            longest = i
    counter = 1

    if i % 10000 == 0:
        print(f'{i/10000}% complete; time = {int(time.time() - t)}secs')
    
print(longest)
    