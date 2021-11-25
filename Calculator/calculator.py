def sum(a, b):
    return a + b
def sub(a, b):
    return sum(a, -b)
def mul(a, b):
    tot = 0
    for i in range(b):
        tot = sum(tot, a)
    return tot
def div(a, b):
    counter = 0
    indent = 1
    while (1==1)==1:
        if a - b >= 0:
            counter += 1/indent
            a = a-b
        if a == 0:
            break
        if a - b < 0:
            a = mul(a, 10)
            indent = mul(indent, 10)
    return counter



print(div(11, 2))
print(eval("0.1+0.2"))