def temp(m, n):
    return num(m+1, n+1)

def num(m, n):
    if m <= 0 or n <= 0: return 0
    if m == 1 and n == 1: return 1
    return num(m-1, n) + num(m, n-1)



def num2(m, n):
    if m < 0 or n < 0: return 0
    elif m == 1 or m == 0 and n == 1 or n == 0: return 2
    return num2(m-1, n) + num2(m, n-1)
    
print(temp(3, 3), num2(3, 3))
