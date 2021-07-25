import random
import time
from threading import Thread

dic = {}
for i in range(26):
    dic[chr(65+i+26+6)]=i+1
print(dic)

score = 0

enter = None

def check():
    time.sleep(5)
    if enter != None:
        return
    print("Too Slow, your score is: ", score)
    quit()

while True:
    letter, index = random.choice(list(dic.items()))
    k = random.randint(0, 1)
    if k == 0:
        enter = int(input(letter + ": " ))
        if enter == index:
            print(True)
            score += 1
        else:
            print("Wrong, it was " + str(index), "Your score is: ", score)
            break
            
    else:
        enter = input(str(index) + ": ")
        if enter == letter:
            print(True)
            score += 1
        else:
            print("Wrong, it was " + letter, "Your score is: ", score)
            break

    