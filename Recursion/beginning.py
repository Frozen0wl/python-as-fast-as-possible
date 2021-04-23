total = 0
for i in range(5):
    total+=i

print(total)

def add(num):
    if num == 1:
        return 1
    else:
        return num + add(num-1)

print(add(4))