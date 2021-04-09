def func(x):
    def func2():
        print(x)

    return func2

x = func(3)
x()

print()

def func(*args, **kwargs):
    pass

x = [1, 23, 236363, 2728]
print(*x)


print()

def func(x, y):
    print(x, y)

pairs = [(1,2), (3,4)]

for pair in pairs:
    func(*pair)

print()

def func(x, y):
    print(x, y)

pairs = [(1,2), (3,4)]

for pair in pairs:
    func(**{'x': 2, 'y': 5})

print(x)

def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5, one = 0, two = 1)