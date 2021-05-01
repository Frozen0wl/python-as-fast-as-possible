def num_of_days(cost, savings, start):
    sum = savings
    day = 0
    while(sum < cost):
        for i in range(7):
            sum += start+i
            day += 1
            if sum > cost:
                break
        start += 1
        print(sum, start, day)
    return day

print(num_of_days(2050, 1200, 10))
# print(num_of_days(10000, 2500, 50))
# print(num_of_days(500, 300, 50))
        
