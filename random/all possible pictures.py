import time
num=16777216
power = "12"
for i in range(6):
    t = time.time()
    power+="0"
    answer = num**int(power)
    caltime = time.time()-t
    print(caltime)
    output = f"{num}^{power}(total time:{time.time()-t})=\n{answer}\n\ntime to save the answer {time.time()-t-caltime}\n\n\n"
    
    with open('AllPossiblePictures', 'a') as f:
            f.write(output + "\n")
    
