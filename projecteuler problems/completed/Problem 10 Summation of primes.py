import math
import time
def is_prime(x): #checks if the parameter given is prime
    if x == 2:
        return True
    if x % 2 == 0 or x < 2:
        return False
    for i in range(3, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    
    return True

total = 2
counter = 2
for i in range(1, 2000000, 2):
    counter += 2
    if is_prime(i):
        total+=i
        
        
    if counter % 100000 == 0:
            print(i, counter)    
        

print(total)