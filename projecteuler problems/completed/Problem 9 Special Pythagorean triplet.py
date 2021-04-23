def pythagorean_triplet():
    for a in range(1, 1000):
        print(a)
        for b in range(1, 1000):
            c = 1000-b - a
            if (a**2 + b**2) == c**2:
                return (a * b * c)

print(pythagorean_triplet())
                