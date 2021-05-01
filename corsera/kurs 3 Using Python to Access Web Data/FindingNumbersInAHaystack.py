import re
file = open('regex_sum_1235243.txt')
x = []
for line in file:
    line = line.rstrip()
    x += re.findall('[0-9]+', line)
total = 0
for item in x:
    total += int(item)
print(x)
print(total)

# for fun

print(sum([]))