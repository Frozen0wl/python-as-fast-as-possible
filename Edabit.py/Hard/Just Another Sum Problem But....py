import time
def just_another_sum_problem(a, b):
    t = time.time()
    sum = 0
    if a > b:
        a, b = b, a
    
    sum = (b-a+1)*(a+b)/2

    return sum, f'time = {round(time.time()-t, 2)}secs'

print(just_another_sum_problem(-1, 9))

# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 10+10+10+10+5
# (9+1)*(9+1-1)/2