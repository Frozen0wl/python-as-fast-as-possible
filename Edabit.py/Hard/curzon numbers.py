def is_curzon(num):
    if (1 + 2**num) % (1 + 2 * num) == 0:
        return True
    else:
        return False

print(is_curzon(5))

# optional solutions

def is_curzon(n):
	return not (2**n + 1) % (2*n + 1)

is_curzon = lambda n: not ((1 << n) + 1) % (2 * n + 1)

