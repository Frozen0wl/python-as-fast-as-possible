def score(dice):
    values = {}
    total = 0
    for score in dice:
        if score in values:
            values[score] += 1
        else:
            values[score] = 1
    
    for element in values:
        if values[element] >= 3:
            if element == 1:
                total += 1000
                values[element] -= 3
            else:
                total += element * 100
                values[element] -= 3
    
    for element in values:
        print(element, values[element])
        if element == 1:
            total += (100 * values[element])
        if element == 5:
            total += (50 * values[element])

    return total
print( score( [2, 3, 4, 6, 2] ), 0)
print( score(  [4, 4, 4, 3, 3] ), 400)
print( score(  [2, 4, 4, 5, 4] ), 450)