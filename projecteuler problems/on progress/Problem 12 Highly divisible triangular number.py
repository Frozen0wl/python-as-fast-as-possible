import time
def divisors(a):
    number_of_factors = 2
    for i in range(2, int(a/2+2)):
        if a % i == 0:
            print(i)
            number_of_factors +=1
    return number_of_factors


print("sum", divisors(12341234234
))
# def triangular_number(num):
    
#     return int(num*(num+1)/2)

# i = 2
# while True:
#     if i % 10 == 0:
#         print(i)
#     output = divisors(triangular_number(i))
#     #print(i, output)
#     with open('Problem_12_output.txt', 'a') as f:
#             f.write(str(output) + "\n")

#     if output >= 500:
#         print(i)
#         break
#     i+=1
    
