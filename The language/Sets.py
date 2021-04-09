x = set()
s = {4, 32, 2, 2} #only works if the set isn't empty
print(s) # removes the extra 2
print(2+2 in s)
s2 = {2, 5, 6, 7}
print(s.union(s2))
print(s.intersection(s2))