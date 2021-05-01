import math

def is_prime(x):
    if x == 2:
        return True
    if x%2 == 0 or x < 2:
        return False

    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def prime_factors(num):
    a = []
    i = 2
    temp = num
    
    bool = True
    while (bool):
        multiple = 1
        # print(a, i)
        
        if is_prime(i) and temp % i == 0:
            temp /= i
            a.append(i)
        else:
            i+=1
        
        for x in a:
            multiple = multiple*x
        bool = multiple != num
        # print(multiple, num)

    return a
print(prime_factors(120))

