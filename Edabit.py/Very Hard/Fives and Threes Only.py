# forgat the part that it has to contain both 5 and 3
def only_5_and_3(n):
    for i in range(n, -1, -5):
        print(i)
        total = 0
        for num in str(i):
            print(num)
            total += int(num)
        if total % 3 == 0:
            return True
    return False


print(only_5_and_3(17))