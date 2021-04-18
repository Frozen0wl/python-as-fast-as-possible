def func(x):
    return x + 5

print(func(2))

func2 = lambda x : x+5

print(func2(2))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(map(lambda x: x+5, a))

print(b)

