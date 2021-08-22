def coin(a):
    if a == 1:
        return 1
    return coin(a-1) *2 +1

print(coin(998))