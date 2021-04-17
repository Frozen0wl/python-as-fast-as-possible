def add_10(x):
    return x+10

def is_odd(x):
    return x % 2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [filter(is_odd, a)]

c = map(add_10, a)