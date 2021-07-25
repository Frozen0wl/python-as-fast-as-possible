def can_sum(target, numbers):
    if target == 0: return True
    if target < 0: return False

    for number in numbers:
        remainder = target - number
        if can_sum(remainder, numbers):
            return True
    return False


print(can_sum(3000, [14, 7]))
