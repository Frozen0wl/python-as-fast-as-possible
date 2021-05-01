def computerpay(hrs, rate):
    total = 0
    if hrs > 40:
        hrs -= 40
        total += (40*rate)
        total += (hrs*rate*1.5)
    else:
        total = hrs*rate

    return total
hrs = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
print("Pay: ", computerpay(hrs, rate))
