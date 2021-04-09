divisible = []

i = 3

number = 600851475143    

while i < number/2+1:
    if(number % i == 0):
        divisible.append(i)
    i += 2

def is_prime(n):

    if(n % 2 == 0):
        return False

    for i in range(3, n, 2):
        if(n % i == 0):
            return False
    return True

for i in divisible:
    if(is_prime(i)):
        print(i)