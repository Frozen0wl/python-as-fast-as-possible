name = input("Enter file name:")
file = open(name)
counter = 0
for line in file:
    if line.startswith("From "):
        counter += 1
        lst = line.split()
        print(lst[1])
print("There were", counter, "lines in the file with From as the first word")