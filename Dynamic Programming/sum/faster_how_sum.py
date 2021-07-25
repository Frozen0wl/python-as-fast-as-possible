def how_sum(target, numbers, memo = {}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    for number in numbers:
        remainder = target-number
        result = how_sum(remainder, numbers)
        if result != None:
            memo[target] = result + [number]
            return memo[target]

    memo[target] = None
    return memo[target]

print(how_sum(300, [7, 14]))