a = 1
b = 2
c = a + b

total = b



while c < 4000000:
    c = a+b
    a = b
    b = c
    
    if(c % 2 == 0):
        total += c

print(total)