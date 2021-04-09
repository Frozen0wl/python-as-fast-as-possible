x = [4, True, 'hi']
print(len(x))
x.append('hello')
x.extend([4,5,5,5,5])
print(x.pop())
print(x.pop(0))
print(x)
print(x[0])
x[0] = not x[0]
print(x[0])

y = x
x[0] = 'hello'
print(x == y)
