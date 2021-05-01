# funktioniert zu langsam
def digits(number):
    total = 0
    for i in range(1, number):
        total += len(str(i))
    return(total)

print(digits(103496754))

