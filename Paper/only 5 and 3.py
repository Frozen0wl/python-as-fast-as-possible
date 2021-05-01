def swap_sort(sortme):
    index = 0 #2
    while index < len(sortme) - 1:
        new_index = sum(x < sortme[index] for x in sortme)
        if index == new_index:
            index += 1
        else:
            sortme[index], sortme[new_index] = sortme[new_index], sortme[index] # 1

a = [6, 3, 9, 7, 4, 1, 8, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
swap_sort(a)
print(a)
