def combinations(*items):
    sum = 1
    for i in items:
        if i != 0:
            sum *= i
    
    return sum

print(combinations(2, 3))