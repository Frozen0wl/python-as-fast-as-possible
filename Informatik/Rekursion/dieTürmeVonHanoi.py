# a c     1 to c    1

# ##                

# a b     1 to b    1
# a c               2
# b c     2 to c    1

# ##

# a c     1 to c    1
# a b               2
# c b     2 to b    1
# a c     3 to c    3
# b a               1
# b c               2
# a c               1

# ##

# a b               1
# a c     1 to b    2
# b c     2 to c    1
# a b     3 to b    3
# c a     4 to c    1
# c b               2
# a b               1
# a c               4
# a c               1
# b a               2
# c a               1
# b c               3
# a b               1
# a c               2
# b c               1
def coinsort(num:int, temp = 0):
    if num > temp:
        temp = num

    if num == 1:
        return (f"{num}")
    
    else:
        return coinsort(num-1) + (f"{num}") + coinsort(num-1)
    
    


print(coinsort(5))
    
# forward 30
# left 45
# forward 30
# back 30
# right 90
# forward 30
# back 30
# left 45
# back 30
# right 90
# forward 30
# left 45
# forward 30
# back 30
# right 90
# forward 30
# back 30
# left 45
# back 30
# left 45
# back 30
# right 90
# forward 30
# left 45
# forward 30
# left 45
# forward 30
# back 30
# right 90
# forward 30
# back 30
# left 45
# back 30
# right 90
# forward 30
# left 45
# forward 30
# back 30
# right 90
# forward 30
# back 30
# left 45
# back 30
# left 45
# back 30
# left 45
# back 30
