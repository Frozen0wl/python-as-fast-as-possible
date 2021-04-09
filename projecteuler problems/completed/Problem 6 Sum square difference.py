import time

start = time.time()
##
num = 100
total_seperate = 0
total_togather = 0

for i in range(num+1):
    total_seperate += i**2
    total_togather += i

    
print(total_togather**2 - total_seperate)


##
end = time.time()


print(end - start)