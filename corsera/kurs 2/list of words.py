name = input('Enter file name:')
romeo = open(name)

lst = list()
for line in romeo:
    stuff = line.split()
    for word in stuff:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)