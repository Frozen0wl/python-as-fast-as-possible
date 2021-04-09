x = [1,2,3,4,5,1,2,4, 1,34,21,14,32,1,432,2]

mp = map(lambda i: i + 2, x)

print(list(mp))

print()

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))