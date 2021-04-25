a = ["A", "B", "B", "B", "A", "A", 'A']
def majority_element(lst):
    maxcount = 0
    variable = None
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        if count > maxcount:
            maxcount = count
            variable = i
    if maxcount > len(lst)/2:
        return variable

print(majority_element(a))

