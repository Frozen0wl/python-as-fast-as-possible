lst = []

for i in range(1, 11):
    lst.append(i)

print(lst)

def func(x):
    return x**x

# x_over_x = []

# for x in lst:
#     x_over_x.append(func(x))

# print(x_over_x)

print(list(map(func, lst)))

print([func(x) for x in lst]) # [] turns it into a list
print([func(x) for x in lst if x % 2 == 0])