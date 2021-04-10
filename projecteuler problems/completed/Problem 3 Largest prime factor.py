import math


divisible = []

i = 3

number = 600851475143    

while i < math.sqrt(number):
    if(number % i == 0):
        divisible.append(i)
        print(i)
    i += 2
    

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x < 2:
        return False
    for i in range (3, x, 2):
        if x % i == 0:
            return False
    print(x)
    return True

for i in divisible:
    if(is_prime(i)):
        print(i)