import math
total = 0
num = str(2**1000)
for char in num:
    total += int(char)

print(total)
print(sum(map(int, str(2**1000))))
mapp = (map(int, str(2**1000)))
for element in mapp:
    print(element)
print(len(num))
print(1+math.log(2**1000, 10 ))
print(math.log(100, 10))