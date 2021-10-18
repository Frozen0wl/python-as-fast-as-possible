name = input("Enter file name: ")
text = open(name)
counter = 0
average = 0
for line in text:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    temp = line.find("0")
    counter += 1
    average += float(line[temp:temp+6])
print("Average spam confidance:", average/counter)
