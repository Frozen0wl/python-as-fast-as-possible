def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x < 2:
        return False
    for i in range (3, x, 2):
        if x % i == 0:
            return False
    return True

num = 0
count = 0

while True:
    num += 1
    if is_prime(num):
        count += 1

    if count == 10001:
        break

print (num)
