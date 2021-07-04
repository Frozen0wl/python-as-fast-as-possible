import time
num = 10**10
def max_ps(num):
    max_ps = int(num**0.5)

    while num % (max_ps*max_ps) != 0:
        max_ps -= 1
    return max_ps*max_ps
start = time.time()
total = 0
previous = time.time()




for i in range(1, num+1):
    if i % (num/1000000) == 0:
        output = (f'{i/(num/100)}% is done | total is: {total} | total time: {format((time.time() - start), ".3f")}secs | previous time: {format((time.time() - previous), ".3f")}secs')
        previous = time.time()
        with open('Problem 745 output.txt', 'a') as f:
            f.write(output + "\n")
    total += max_ps(i)
    # print(max_ps(i))

print(total)

