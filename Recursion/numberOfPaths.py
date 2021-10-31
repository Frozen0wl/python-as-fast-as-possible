def nop(n, m):
    if n == 1 or m == 1: return 1
    return nop(n-1, m)+nop(n, m-1)

print(nop(2 , 3))

