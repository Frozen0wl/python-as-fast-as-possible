def consecutive_combo(lst1, lst2):
    lst = lst1 + lst2

    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    print(lst)

    for i in range(1, len(lst)):
        if lst[i-1] + 1 != lst[i]:
            return False
    return True
print(consecutive_combo([1, 5, 2], [4, 6, 3]))


# elegant solution
# def consecutive_combo(lst1, lst2):
	# lst3 = lst1 + lst2
	# return max(lst3) - min(lst3) == len(lst3) - 1