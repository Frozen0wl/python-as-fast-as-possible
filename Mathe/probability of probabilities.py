import random
from pprint import pprint


s = 0.95

n = 50

numberOfRuns = 250000 # https://www.desmos.com/calculator/864j4ymjid?lang=de

occurrance = {}
distribution = {}
def instance():
    lst = []
    for i in range(n):
        if random.random()<s:
            lst.append(1)
        else:
            lst.append(0)

    return( lst.count(1))

for i in range(numberOfRuns):
    num = instance()
    if num in occurrance:
        occurrance[num] += 1
    else:
        occurrance[num] = 1


for key in occurrance:
    distribution[key] = str(round((occurrance[key]/numberOfRuns)*100, 4))+"%"
    

# pprint(occurrance)
pprint(distribution)