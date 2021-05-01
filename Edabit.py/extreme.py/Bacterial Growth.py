def bacteria(final_mass):
    tag = 1
    while 2**tag - 1 < final_mass:
        tag+=1
    return tag - 1




# if split:
#     mass += n*2
# if not split:
#     mass += n

# m = 1
# n = 1

# n = 2
# m = 3


# n = 1
# m = 1
# gm = 1  # 2^1 - 1

# ---

# n = 2
# m = 0.5
# m = 1.5
# gm = 3 # 2^2 - 1
# ---

# n = 4
# m = 0.75
# m = 1.75
# gm = 7 # 2^3 - 1
# ---

# n = 8
# m = 0.875
# m = 1.875
# gm = 15 # 2^4 - 1

# ---

# n = 16
# m = 0.9375
# m = 1.9375
# gm = 31 # 2^tag - 1

# =========



