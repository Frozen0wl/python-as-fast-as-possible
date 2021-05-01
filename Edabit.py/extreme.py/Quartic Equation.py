import math
def quartic_equation(a, b, c):
    lst = []
    xone = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    xtwo = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    try:
        lst.append(math.sqrt(xone))   
    except:
        pass
    try:
        lst.append(math.sqrt(xtwo))
    except:
        pass
    try:
        lst.append(math.sqrt(xone)*(-1))
    except:
        pass
    try:
        lst.append(math.sqrt(xtwo)*(-1))
    except:
        pass
    
    lstlast = []
    for i in lst:
        if i not in lstlast:
            lstlast.append(i)

    return len(lstlast)
print(quartic_equation(1, -5, 4))
print(quartic_equation(4, 3, -1))
print(quartic_equation(9, -4, 0))