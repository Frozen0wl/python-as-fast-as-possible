x = [x for x in range(5)]
print(x)

print()
x = [[0 for x in range(5)] for x in range(2)]
print(x)

print()

x = [i for i in range(100) if i % 5 == 0]
print(x)

print()

x = {i:0 for i in range(100) if i % 5 == 0}
print(x)