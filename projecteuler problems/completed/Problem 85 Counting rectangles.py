import math
def num_rectangles(a, b):
    a = a+1
    b = b+1
    return (((a*(a-1))/2)*((b*(b-1))/2))

closest = [20000000, (10, 20)]
for i in range(1, 100):
    for j in range(1, 100):
        if abs(num_rectangles(i, j)-2000000) < closest[0]:
            closest[0], closest[1] = abs(num_rectangles(i, j)-2000000), (i, j)
        #print(abs(num_rectangles(i, j)-2000000), (i, j))
print(closest[1][1]*closest[1][0])
