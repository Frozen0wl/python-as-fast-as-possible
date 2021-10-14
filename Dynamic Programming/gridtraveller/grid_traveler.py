def grid_traveler(m, n):
    if m <= 0 or n <= 0: return 0
    if m == 1 and n == 1: return 1
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

print(grid_traveler(2, 6))
# print(grid_traveler(4, 5)+(grid_traveler(5, 4)))

# for i in range(3, 10):
#     print(grid_traveler(i, i))