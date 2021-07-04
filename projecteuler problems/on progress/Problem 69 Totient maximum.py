import time
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def relatively_prime(num):
    count = 0
    for i in range(num):
        if gcd(num, i) == 1:
            count+=1
    return count

max = 0
num = 1000001
start = time.time()
for i in range(2, num):
    
    cal = i/relatively_prime(i)
    if cal>max:
        max = cal
        maxval = i
    if i % 1000 == 0:
        print(f'{i/10000}% is complete; max = {maxval}; total time = {int(time.time()-start)}secs')
        print(f'max is {max} and current is {cal}\n')

print(max)