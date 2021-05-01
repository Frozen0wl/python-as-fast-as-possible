# not returning x
def super_digit(n, k):
    p = str(n)*k
    # print("p is", p)
    x = 0
    temp =  0
    for digits in p:
        x = x + int(digits)
    # print("x is ", x)
    if len(str(x)) == 1:
        # print(x)
        return x
    else:
        return(super_digit(x, 1))
print(super_digit(148, 3))