import collections
from collections import Counter



c = Counter(['a', 'b', 'c', 'a'])
print(c)
d = ['a','b','d']
# print(c.most_common(2))
c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear
print(c)

y = Counter(a = 4, b = 2, c = 0, d = -2)
print(c+y)
print(c-y)
print(c & y)
print(c| d)
