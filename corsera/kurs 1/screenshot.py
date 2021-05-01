largest  = 5
smallest = 5
while True:
    num = input("Enter a number: ")
    if num == "done": break

    try:
        temp = float(num)
    except:
        print("Invalid input")
        continue
    if temp > largest or largest == None:
        largest = temp
    if temp < smallest or smallest == None:
        smallest = temp
    
    
print("Maximum is", largest)
print("Minumun is", smallest)

