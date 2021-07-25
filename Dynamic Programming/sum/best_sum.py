def best_sum(target, numbers, memo = {}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortest = None

    for number in numbers:
        remainder = target - number
        result = best_sum(remainder, numbers)
        if result != None:
            combination = result + [number]
            if shortest == None or len(combination) < len(shortest):
                shortest = combination
    memo[target] = shortest
    return shortest
        
print(best_sum(100, [1, 2, 5, 25]))