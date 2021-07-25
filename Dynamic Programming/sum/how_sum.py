def how_sum(target, numbers):
    if target == 0: return []
    if target < 0: return None
    
    for number in numbers:
        remainder = target-number
        result = how_sum(remainder, numbers)
        if result != None:
            return result + [number]

    return None

print(how_sum(300, [7, 13]))