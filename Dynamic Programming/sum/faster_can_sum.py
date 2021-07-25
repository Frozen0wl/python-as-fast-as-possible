def can_sum(target, numbers, memo = {}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for number in numbers:
        remainder = target - number
        if can_sum(remainder, numbers):
            memo[target] = True
            return True
    memo[target] = False
    return False


print(can_sum(3000, [14, 7]))
