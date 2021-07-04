import random
#print(random.randint(1,7))

lst = []

### fill list with 10 of each number###
for j in range(10):
    for i in range(1, 8):
        lst.append(i)

###take 20 random balls and identify number of distinc ones###
sum = 0
count = 0

for i in range(10000000):
    lst20 = []
    for j in range(20):
        lst20.append(lst[random.randint(0,69)])
    lstdist = []
    for elements in lst20:
        if elements not in lstdist:
            lstdist.append(elements)
    sum += len(lstdist)
    count += 1
    if i % 10000 == 0:
        print(f'{i/100000}% is complete')
print(sum/count)    

    


    
