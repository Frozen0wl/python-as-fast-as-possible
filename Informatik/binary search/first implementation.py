import math
a = []
for i in range(1000):
    a.append(i)

key = 695

for i in range(int(math.sqrt(len(a)))):
    if key > a[int(len(a/2))]:
        a = a[int(len(a/2)):int(len(a))]
    else:
        a = a[0:len(a)]

print(a)



