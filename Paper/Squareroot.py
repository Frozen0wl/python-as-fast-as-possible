def squareroot(num, temp):
    a = (1/2)*(temp+(num/temp))
    print(a)
    squareroot(num, a)

squareroot(16, 20)