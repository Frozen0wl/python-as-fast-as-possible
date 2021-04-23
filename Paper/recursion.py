def fun1(x, y) :
 
    if (x == 0) :
        return y
    else :
        return fun1(x - 1, x + y)

def fun2(x):
    return((x+1)*x/2)
print(fun1(6, 0), fun2(6))