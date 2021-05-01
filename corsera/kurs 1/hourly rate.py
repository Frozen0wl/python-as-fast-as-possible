hrs = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
total = 0
if hrs > 40:
    hrs -= 40
    total += (40*rate)
    total += (hrs*rate*1.5)
else:
    total = hrs*rate

print(total)
