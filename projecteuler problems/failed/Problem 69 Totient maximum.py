# Works but takes too long

def relatively_prime(num):
    lst = []
    
    for i in range(1, num):
        bool = True
        if i == 1: 
            lst.append(i)
            continue
        elif num % i == 0: continue
        for j in range(2, i):
            if num % j == 0 and i % j == 0:
                bool = False
                break
        if bool == True:
            lst.append(i)
            
    return lst

max = 0
for i in range(2, 10000):
    if i/len(relatively_prime(i))>max:
        max = i
        print(max)
    if i % 100 == 0:
        print(f'{i/100}%% is complete')
print(max)


            
            