def fib_num(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib_num(n-1) + fib_num(n-2)
    return memo[n]

print(fib_num(700))