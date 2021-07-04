def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    else:
        return fib(n-1)+fib(n-2)


fib(5)
fib(4) + fib(3)
fib(3) + fib (2) + fib(2) + fib(1)
fib(2) + fib(1) + 1 + 1 + 1
print(fib(100))

# for i in range(1, 10):
#     print(fib(i), end = " ")
