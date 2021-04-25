def pentagonal(num):
    temp = 0
    if num == 1:
        return 1
    else:
        return pentagonal(num-1) + 5 * (num-1)

print(pentagonal(8))