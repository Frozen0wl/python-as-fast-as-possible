def prime_factors(num):
    a = []
    while num > 1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                a.append(i)
                num = int(num/i)
                break
    return a

print(prime_factors(20))

