import time
def divisors(a):
    number_of_factors = 0
    for i in range(2, int(a/2+2)):
        if a % i == 0:
            number_of_factors +=1
    return number_of_factors

    

temp = 2
triangular_num = 1

while True:
    triangular_num += temp
    temp += 1
    

    if divisors(triangular_num) >= 500:
        print(triangular_num)
        break
    
