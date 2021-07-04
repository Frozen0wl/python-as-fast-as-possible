sum = 0
biggest = 0
list = [1, 2]
for i in range(101):
    for j in range(101):
        for char in str(i**j):
            sum += int(char)
        if sum > biggest:
            biggest = sum
            list[0], list[1] = i, j
    print(i)

print(biggest, list)
