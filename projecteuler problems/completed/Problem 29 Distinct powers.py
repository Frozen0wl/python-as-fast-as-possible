lst = []

def powers(a, b):
    for i in range(2, a+1):
        for j in range(2, b+1):
            pro = i**j
            if pro not in lst:
                lst.append(pro)
    print(len(lst))
    
powers(100, 100)

